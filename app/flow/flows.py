from app.actions.actionsInt import ActionsInt
from abc import ABC, abstractmethod


class FlowInt:
    def __init__(self, actions: ActionsInt):
        self.actions = actions


class LoginFlow(FlowInt,ABC):
    @abstractmethod
    def login(self):
        pass

class SellerFlow(FlowInt,ABC):
    @abstractmethod
    def seller(self):
        pass

class ProductFlow(FlowInt,ABC):
    @abstractmethod
    def product(self):
        pass

class ClientFlow(FlowInt,ABC):
    @abstractmethod
    def client(self):
        pass

class PaymentPlanFlow(FlowInt,ABC):
    @abstractmethod
    def payment_plan(self):
        pass

class DocumentFlow(FlowInt,ABC):
    @abstractmethod
    def document(self):
        pass


class TransmitFlow(FlowInt,ABC):
    @abstractmethod
    def transmit(self):
        pass