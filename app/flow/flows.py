from app.actions.actionsInt import ActionsInt
from abc import ABC, abstractmethod
from pathlib import Path
from app.config.exceptions import IMGDoesntExistError
from app.config.config import settings

class FlowInt(ABC):
    def __init__(self, actions: ActionsInt):
        self.actions = actions

class FlowAbs(FlowInt):
    base_path:str = settings.img_path if settings.img_path else ""

    def _enshure_paths_exist(self, paths_to:list[str]) -> None | Exception:
        for pst in paths_to:
            p = Path(settings.img_path + pst)
            if not (p.exists() and p.is_file()):
                raise IMGDoesntExistError(pst)


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