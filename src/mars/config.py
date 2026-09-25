"""Application configuration."""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    environment: str = os.getenv("MARS_ENV", "development")
    log_level: str = os.getenv("MARS_LOG_LEVEL", "INFO")
    database_url: str = os.getenv(
        "MARS_DATABASE_URL",
        "sqlite:///data/mars.db",
    )


settings = Settings()
