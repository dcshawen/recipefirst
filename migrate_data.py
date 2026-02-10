#!/usr/bin/env python3
"""
Data migration script to copy data from SQLite to PostgreSQL.

This script:
1. Connects to both SQLite and PostgreSQL databases
2. Reads all data from SQLite
3. Writes data to PostgreSQL preserving relationships
4. Maintains foreign key constraints and XOR constraints

Usage:
    # Set environment variable for PostgreSQL
    export DATABASE_URL="postgresql+asyncpg://user:pass@host:5432/dbname"

    # Run migration
    python migrate_data.py
"""

import asyncio
import sys
import os
from pathlib import Path
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from data.models import (
    Base, UnitType, Category, Ingredient, FoodItem, Recipe,
    RecipeInstruction, RecipeIngredient, Meal, MealFoodItem,
    RecipeCategory, IngredientCategory, MealCategory
)


class DataMigrator:
    """Handles migration of data from SQLite to PostgreSQL."""

    def __init__(self, sqlite_url: str, postgres_url: str):
        self.sqlite_url = sqlite_url
        self.postgres_url = postgres_url
        self.sqlite_engine = None
        self.postgres_engine = None

    async def setup_connections(self):
        """Create database connections."""
        print(f"Connecting to SQLite: {self.sqlite_url}")
        self.sqlite_engine = create_async_engine(self.sqlite_url, echo=False)

        print(f"Connecting to PostgreSQL: {self.postgres_url}")
        self.postgres_engine = create_async_engine(self.postgres_url, echo=False)

    async def close_connections(self):
        """Close database connections."""
        if self.sqlite_engine:
            await self.sqlite_engine.dispose()
        if self.postgres_engine:
            await self.postgres_engine.dispose()

    async def copy_table_data(self, model, session_maker_src, session_maker_dst):
        """
        Copy all data from one table to another.

        Args:
            model: SQLAlchemy model class
            session_maker_src: Source database session maker
            session_maker_dst: Destination database session maker
        """
        table_name = model.__tablename__
        print(f"  Migrating {table_name}...", end=" ")

        # Read from source
        async with session_maker_src() as session:
            result = await session.execute(select(model))
            records = result.scalars().all()

        if not records:
            print("(no data)")
            return 0

        # Write to destination
        async with session_maker_dst() as session:
            for record in records:
                # Create a new instance with the same data
                record_dict = {}
                for column in model.__table__.columns:
                    record_dict[column.name] = getattr(record, column.name)

                new_record = model(**record_dict)
                session.add(new_record)

            await session.commit()

        count = len(records)
        print(f"({count} records)")
        return count

    async def migrate_all_data(self):
        """Migrate all data in the correct order to preserve foreign keys."""
        print("\n=== Starting Data Migration ===\n")

        sqlite_session = sessionmaker(
            self.sqlite_engine, class_=AsyncSession, expire_on_commit=False
        )
        postgres_session = sessionmaker(
            self.postgres_engine, class_=AsyncSession, expire_on_commit=False
        )

        # Migration order: Foundation tables first, then dependent tables
        migration_order = [
            # Core entities (no dependencies)
            ("UnitType", UnitType),
            ("Category", Category),
            ("Ingredient", Ingredient),
            ("FoodItem", FoodItem),

            # Recipe and dependent tables
            ("Recipe", Recipe),
            ("RecipeInstruction", RecipeInstruction),
            ("RecipeIngredient", RecipeIngredient),  # Depends on Recipe, Ingredient, FoodItem, UnitType

            # Meal and dependent tables
            ("Meal", Meal),
            ("MealFoodItem", MealFoodItem),

            # Junction tables for categories
            ("RecipeCategory", RecipeCategory),
            ("IngredientCategory", IngredientCategory),
            ("MealCategory", MealCategory),
        ]

        total_records = 0

        for table_name, model in migration_order:
            count = await self.copy_table_data(model, sqlite_session, postgres_session)
            total_records += count

        print(f"\n=== Migration Complete ===")
        print(f"Total records migrated: {total_records}")

    async def verify_migration(self):
        """Verify that data was migrated correctly."""
        print("\n=== Verifying Migration ===\n")

        sqlite_session = sessionmaker(
            self.sqlite_engine, class_=AsyncSession, expire_on_commit=False
        )
        postgres_session = sessionmaker(
            self.postgres_engine, class_=AsyncSession, expire_on_commit=False
        )

        models_to_verify = [
            UnitType, Category, Ingredient, FoodItem, Recipe,
            RecipeInstruction, RecipeIngredient, Meal, MealFoodItem,
            RecipeCategory, IngredientCategory, MealCategory
        ]

        all_match = True

        for model in models_to_verify:
            table_name = model.__tablename__

            # Count records in both databases
            async with sqlite_session() as session:
                result = await session.execute(select(model))
                sqlite_count = len(result.scalars().all())

            async with postgres_session() as session:
                result = await session.execute(select(model))
                postgres_count = len(result.scalars().all())

            status = "✓" if sqlite_count == postgres_count else "✗"
            print(f"  {status} {table_name}: SQLite={sqlite_count}, PostgreSQL={postgres_count}")

            if sqlite_count != postgres_count:
                all_match = False

        if all_match:
            print("\n✓ All tables migrated successfully!")
        else:
            print("\n✗ Some tables have mismatched record counts!")

        return all_match


async def main():
    """Main migration entry point."""
    # SQLite database path (existing database)
    sqlite_path = Path(__file__).parent / 'data' / 'instances' / 'recipefirst.db'
    sqlite_url = f"sqlite+aiosqlite:///{sqlite_path}"

    # PostgreSQL URL from environment variable
    postgres_url = os.getenv("DATABASE_URL")

    if not postgres_url:
        print("ERROR: DATABASE_URL environment variable not set")
        print("Example: export DATABASE_URL='postgresql+asyncpg://user:pass@localhost:5432/recipefirst'")
        sys.exit(1)

    if not postgres_url.startswith("postgresql"):
        print("ERROR: DATABASE_URL must be a PostgreSQL connection string")
        sys.exit(1)

    if not sqlite_path.exists():
        print(f"ERROR: SQLite database not found at {sqlite_path}")
        sys.exit(1)

    print("=" * 60)
    print("RecipeFirst Data Migration: SQLite → PostgreSQL")
    print("=" * 60)
    print(f"\nSource: {sqlite_url}")
    print(f"Target: {postgres_url}")
    print("\nWARNING: This will copy all data from SQLite to PostgreSQL.")
    print("Make sure you have run 'alembic upgrade head' first!\n")

    response = input("Continue? (yes/no): ")
    if response.lower() not in ['yes', 'y']:
        print("Migration cancelled.")
        sys.exit(0)

    migrator = DataMigrator(sqlite_url, postgres_url)

    try:
        await migrator.setup_connections()
        await migrator.migrate_all_data()
        success = await migrator.verify_migration()

        if success:
            print("\n✓ Migration completed successfully!")
            sys.exit(0)
        else:
            print("\n✗ Migration completed with errors!")
            sys.exit(1)

    except Exception as e:
        print(f"\n✗ Migration failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        await migrator.close_connections()


if __name__ == "__main__":
    asyncio.run(main())
