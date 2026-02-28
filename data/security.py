"""
Security and authentication functions for the RecipeFirst application.
Handles password hashing, verification, JWT generation, and token decoding.
"""

from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, Any

from jose import JWTError, jwt
from passlib.context import CryptContext

from .config import settings

# Configure passlib to use bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a hashed password.
    
    Args:
        plain_password (str): The plain text password.
        hashed_password (str): The previously hashed password.
        
    Returns:
        bool: True if passwords match, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Generate a password hash from a plain text password.
    
    Args:
        password (str): The plain text password.
        
    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)


# ============================================================================
# JWT Utilities
# ============================================================================

def create_access_token(
    data: Dict[str, Any],
    expires_delta: Optional[timedelta] = None,
) -> str:
    """
    Create a signed JWT access token.

    Tokens do not expire by default — they remain valid until the user logs
    out (or the secret key is rotated).  Pass ``expires_delta`` to add an
    ``exp`` claim when a bounded lifetime is needed.

    Args:
        data: Payload claims to encode.  Typically includes ``sub`` (the
              string representation of the user's ID).
        expires_delta: Optional expiry duration.  If omitted, no ``exp``
              claim is added and the token never expires.

    Returns:
        Encoded JWT string.
    """
    payload = data.copy()
    if expires_delta is not None:
        payload["exp"] = datetime.now(timezone.utc) + expires_delta
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


def decode_access_token(token: str) -> Dict[str, Any]:
    """
    Decode and validate a JWT access token.

    Args:
        token: Encoded JWT string.

    Returns:
        The decoded payload dictionary.

    Raises:
        JWTError: If the token is invalid, expired, or the signature does
                  not match.
    """
    return jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])


def get_subject_from_token(token: str) -> Optional[str]:
    """
    Convenience wrapper that returns only the ``sub`` claim.

    Returns:
        The ``sub`` string, or ``None`` if the claim is absent or the token
        is invalid.
    """
    try:
        payload = decode_access_token(token)
        return payload.get("sub")
    except JWTError:
        return None
