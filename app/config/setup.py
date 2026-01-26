import pyautogui
import os
from typing import Any
from app.config.config import EnvironmentSettings,PyAutoGUISettings,CredentialsSettings, IMGBasePathSettings

def configure(
    settings:
        EnvironmentSettings
        | PyAutoGUISettings
        | CredentialsSettings
        | IMGBasePathSettings,
    **kwargs: Any,    
):
    if isinstance(settings,PyAutoGUISettings):
        pyautogui.FAILSAFE = settings.FAILSAFE
        pyautogui.PAUSE = settings.PAUSE
    if isinstance(settings, IMGBasePathSettings):
        if not os.path.isdir(settings.img_path):
            os.makedirs(settings.img_path)

            

