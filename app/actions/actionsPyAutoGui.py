import pyautogui
from app.actions.actionsInt import ActionsInt
from app.config.config import settings


class ActionPyAutoGUIImpl(ActionsInt):
    def search(self,path_to_img:str):
        return pyautogui.locateCenterOnScreen(path_to_img,confidence=settings.confidance)

    def left_click(self, x:int,y:int, clicks:int = 1):
        pyautogui.click(x=x,y=y,button="left",clicks=clicks)

    def right_click(self, x:int, y:int, clicks:int = 1):
        pyautogui.click(x=x,y=y,button="right",clicks = clicks)

    def write(self,text:str,interval = 0.3):
        pyautogui.typewrite(text,interval=0.3)

def getActionPyAutoGUIImpl() -> ActionsInt:
    return ActionPyAutoGUIImpl()