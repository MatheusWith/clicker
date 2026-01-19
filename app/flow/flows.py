from app.actions.actionsInt import ActionsInt
from abc import ABC, abstractmethod


class Flow:
    def __init__(self, actions: Actions):
        self.actions = actions


class LoginFlow(Flow,ABC):
    @abstractmethod
    def login(self):
        pass

