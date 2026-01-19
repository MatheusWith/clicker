import pyautogui
from app.flows.action import Actions


class ActionPyAutoGUIImpl(Actions):
    def search(self,path_to_img:str):
        return pyautogui.locateCenterOnScreen(path_to_img)

    def left_click(self, x:int,y:int, clicks:int = 1):
        pyautogui.click(x=x,y=y,button="left",clicks=clicks)

    def right_click(self, x:int, y:int, clicks:int = 1):
        pyautogui.click(x=x,y=y,button="right",clicks = clicks)

    def write(self,text:str):
        pyautogui.typewrite(text,interval=0.5)

def getActionPyAutoGUIImpl() -> Actions:
    return ActionPyAutoGUIImpl()