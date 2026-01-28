from app.actions.actionsInt import ActionsInt
from abc import ABC, abstractmethod
from pathlib import Path
from app.config.exceptions import IMGDoesntExistError
from app.config.config import settings

class FlowInt(ABC):
    def __init__(self, actions: ActionsInt):
        self.actions = actions

    @abstractmethod
    def execute(self):
        pass

class FlowAbs(FlowInt):
    base_path:str = settings.img_path if settings.img_path else ""

    def _enshure_paths_exist(self, paths_to:list[str]) -> None | Exception:
        for pst in paths_to:
            p = Path(settings.img_path + pst)
            if not (p.exists() and p.is_file()):
                raise IMGDoesntExistError(pst)


class OpenFlow(FlowAbs,ABC):
    pass


class LoginFlow(FlowAbs,ABC):
    pass


class SellerFlow(FlowAbs,ABC):
    pass


class ProductFlow(FlowAbs,ABC):
    pass


class ClientFlow(FlowAbs,ABC):
    pass


class PaymentPlanFlow(FlowAbs,ABC):
    pass


class DocumentFlow(FlowAbs,ABC):
    pass


class TransmitFlow(FlowAbs,ABC):
    pass


class FinishFlow(FlowAbs,ABC):
    pass