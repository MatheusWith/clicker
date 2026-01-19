from __future__ import annotations
from abc import ABC, abstractmethod


class Actions(ABC):
    @abstractmethod
    def search(self,path_to_img:str) -> tuple[int,int]:
        pass

    @abstractmethod
    def left_click(self,x: int, y: int) -> None:
        pass

    @abstractmethod
    def right_click(self, x:int, y:int) -> None:
        pass

    @abstractmethod
    def write(self, text: str) -> None:
        pass
