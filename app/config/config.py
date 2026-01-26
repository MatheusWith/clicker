import os
from enum import Enum
from pydantic_settings import BaseSettings, SettingsConfigDict


class CredentialsSettings(BaseSettings):
    LOGIN: str
    PASSWORD: str

class DataParameterSettings(BaseSettings):
    START_DATE:str
    END_DATE:str

class PyAutoGUISettings(BaseSettings):
    FAILSAFE: bool = True
    PAUSE: float = 2.5
    CONFIDANCE:float = 0.8


class EnvironmentOption(str, Enum):
    LOCAL = "local"
    STAGING = "staging"
    PRODUCTION = "production"


class EnvironmentSettings(BaseSettings):
    ENVIRONMENT: EnvironmentOption = EnvironmentOption.LOCAL

class IMGBasePathSettings(BaseSettings):
    img_path:str = "app/img/"


class Settings(
    EnvironmentSettings,
    PyAutoGUISettings,
    CredentialsSettings,
    DataParameterSettings,
    IMGBasePathSettings,
):
    model_config = SettingsConfigDict(
        env_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),"..","..",".env"),
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()