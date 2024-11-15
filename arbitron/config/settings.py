from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Application settings."""
    
    # API Configuration
    API_KEY: Optional[str] = None
    API_SECRET: Optional[str] = None
    
    # Trading Configuration
    MAX_POSITION_SIZE: float = 1000.0
    RISK_TOLERANCE: float = 0.02
    
    # Database Configuration
    DATABASE_URL: Optional[str] = None
    
    class Config:
        env_file = ".env" 