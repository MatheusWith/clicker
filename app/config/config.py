import os
from enum import Enum
from pydantic_settings import BaseSettings, SettingsConfigDict

class PyAutoGUISettings(BaseSettings):
    FAILSAFE: bool = True
    PAUSE: int = 2.5


class EnvironmentOption(str, Enum):
    LOCAL = "local"
    STAGING = "staging"
    PRODUCTION = "production"


class EnvironmentSettings(BaseSettings):
    ENVIRONMENT: EnvironmentOption = EnvironmentOption.LOCAL


class Settings(
    EnvironmentSettings,
    PyAutoGUISettings,
):
    model_config = SettingsConfigDict(
        env_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),"..","..",".env"),
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()