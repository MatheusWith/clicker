import pyautogui
from typing import Any
from app.core.config import (
    EnvironmentSettings,
    PyAutoGUISettings,
    settings,
)


def configure(
    settings:(
        EnvironmentSettings,
        PyAutoGUISettings,
    ),
    **kwargs: Any,    
):
    if isinstance(settings,PyAutoGUISettings):
        pyautogui.FAILSAFE = settings.FAILSAFE
        pyautogui.PAUSE = settings.PAUSE
