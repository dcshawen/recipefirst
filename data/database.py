"""
Database engine and session management for RecipeFirst application.

This module provides:
- Async SQLAlchemy engine configuration
- Session factory for dependency injection
- FastAPI dependency for database sessions
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.pool import StaticPool
from pathlib import Path
from typing import AsyncGenerator
import logging

# Setup logging
logger = logging.getLogger(__name__)

# Construct database path
current_dir = Path(__file__).parent
db_path = current_dir / 'instances' / 'recipefirst.db'

# Ensure instances directory exists
db_path.parent.mkdir(parents=True, exist_ok=True)

# SQLite async connection string
DATABASE_URL = f"sqlite+aiosqlite:///{db_path}"

logger.info(f"Database URL: {DATABASE_URL}")

# Create async engine
# For SQLite, we use StaticPool to ensure single connection for file locking
engine = create_async_engine(
    DATABASE_URL,
    echo=False,  # Set to True for SQL query logging (useful for debugging)
    future=True,
    # SQLite-specific: use StaticPool for async + file-based DB
    poolclass=StaticPool,
    connect_args={
        "check_same_thread": False  # Required for SQLite async
    }
)

# Create async session factory
# expire_on_commit=False prevents SQLAlchemy from expiring objects after commit,
# which is useful for async as we may access them outside the session context
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    FastAPI dependency that provides a database session.

    Usage in routes:
        @router.get("/recipes")
        async def get_recipes(db: AsyncSession = Depends(get_db)):
            ...

    The session is automatically:
    - Created at the start of the request
    - Committed if no exceptions occur
    - Rolled back if exceptions occur
    - Closed at the end of the request
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            logger.error(f"Database session error: {e}")
            raise
        finally:
            await session.close()


async def init_db():
    """
    Initialize database by creating all tables.

    Note: This should only be used for development/testing.
    For production, use Alembic migrations instead.
    """
    from models import Base

    async with engine.begin() as conn:
        # Drop all tables (use with caution!)
        # await conn.run_sync(Base.metadata.drop_all)

        # Create all tables
        await conn.run_sync(Base.metadata.create_all)

    logger.info("Database tables created successfully")


async def close_db():
    """
    Close all database connections.

    Should be called on application shutdown.
    """
    await engine.dispose()
    logger.info("Database connections closed")
