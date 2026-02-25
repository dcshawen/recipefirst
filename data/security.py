"""
Security and authentication functions for the RecipeFirst application.
Handles password hashing and verification.
"""

from passlib.context import CryptContext

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
