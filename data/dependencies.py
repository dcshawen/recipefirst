"""
FastAPI dependencies for RecipeFirst application.

Provides reusable Depends()-compatible functions, including the JWT
authentication dependency used to protect endpoints that require a
logged-in user.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from .database import get_db
from .security import decode_access_token
from . import crud
from .models import User

# Tells FastAPI where clients obtain a token; used for OpenAPI docs.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: AsyncSession = Depends(get_db),
) -> User:
    """
    Decode the Bearer JWT and return the corresponding User ORM object.

    Raises:
        401 Unauthorized: If the token is missing, malformed, expired, or
                          the ``sub`` claim does not map to a known user.
        403 Forbidden:    If the user account is inactive.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id_str: str | None = payload.get("sub")
        if user_id_str is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    try:
        user_id = int(user_id_str)
    except ValueError:
        raise credentials_exception

    user = await crud.get_user_by_id(session, user_id)
    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is inactive",
        )

    return user
