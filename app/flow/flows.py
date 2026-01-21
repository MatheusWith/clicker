from app.actions.actionsInt import ActionsInt
from abc import ABC, abstractmethod


class Flow:
    def __init__(self, actions: ActionsInt):
        self.actions = actions


class LoginFlow(Flow,ABC):
    @abstractmethod
    def login(self):
        pass

class SellerFlow(Flow,ABC):
    @abstractmethod
    def seller(self):
        pass

class ProductFlow(Flow,ABC):
    @abstractmethod
    def product(self):
        pass

class ClientFlow(Flow,ABC):
    @abstractmethod
    def client(self):
        pass

class PlanoPagamento(Flow,ABC):
    @abstractmethod
    def plano_pagamento(self):
        pass