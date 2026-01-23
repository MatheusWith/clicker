from app.actions.actionsInt import ActionsInt
from abc import ABC, abstractmethod


class FlowAbs:
    def __init__(self, actions: ActionsInt):
        self.actions = actions


class LoginFlow(FlowAbs,ABC):
    @abstractmethod
    def login(self):
        pass

class SellerFlow(FlowAbs,ABC):
    @abstractmethod
    def seller(self):
        pass

class ProductFlow(FlowAbs,ABC):
    @abstractmethod
    def product(self):
        pass

class ClientFlow(FlowAbs,ABC):
    @abstractmethod
    def client(self):
        pass

class PaymentPlanFlow(FlowAbs,ABC):
    @abstractmethod
    def payment_plan(self):
        pass

class DocumentFlow(FlowAbs,ABC):
    @abstractmethod
    def document(self):
        pass


class TransmitFlow(FlowAbs,ABC):
    @abstractmethod
    def transmit(self):
        pass