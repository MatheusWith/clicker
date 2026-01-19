from app.actions.actionsInt import Actions
from abc import ABC, abstractmethod


class Flow:
    def __init__(self, actions: Actions):
        self.actions = actions


class LoginFlow(Flow,ABC):
    @abstractmethod
    def login(self):
        pass

