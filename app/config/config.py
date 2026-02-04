import os
from enum import Enum
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class CredentialsSettings(BaseSettings):
    LOGIN: str
    PASSWORD: str

class DataParameterSettings(BaseSettings):
    START_DATE:str
    END_DATE:str

class ToFieldSettings(BaseSettings):
    MTF_SELLER:int
    MTF_LOGIN:int
    
class PyAutoGUISettings(BaseSettings):
    FAILSAFE: bool = True
    PAUSE: float = 2.5
    CONFIDANCE:float = 0.8

    @field_validator("CONFIDANCE")
    @classmethod
    def validate_confidance(cls, v:float) -> float:
        if not 0 <= v <= 1:
            raise ValueError("CONFIDANCE must be between 0.0 to 1.0")
        return v

    @field_validator("PAUSE")
    @classmethod
    def validate_pause(cls,v:float) -> float:
        if v < 0:
            raise ValueError("PAUSE doenst is negative")
        return v


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
    ToFieldSettings,
):
    model_config = SettingsConfigDict(
        env_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),"..","..",".env"),
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()