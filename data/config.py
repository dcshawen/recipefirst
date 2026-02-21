"""
Configuration management for RecipeFirst application.

This module provides environment variable configuration using Pydantic Settings.
"""

from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings with environment variable support."""

    # Database configuration
    database_url: str = "sqlite+aiosqlite:///data/instances/recipefirst.db"

    # CORS configuration
	cors_origins: List[str] = ["http://localhost:5173", "http://localhost", "http://16.52.119.18:5173"]

    # API configuration
    api_title: str = "RecipeFirst API"
    api_version: str = "1.0.0"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Global settings instance
settings = Settings()
