import pyautogui
from typing import Any
from app.config.config import EnvironmentSettings,PyAutoGUISettings,CredentialsSettings

def configure(
    settings:
        EnvironmentSettings
        | PyAutoGUISettings,
    **kwargs: Any,    
):
    if isinstance(settings,PyAutoGUISettings):
        pyautogui.FAILSAFE = settings.FAILSAFE
        pyautogui.PAUSE = settings.PAUSE
