from pathlib import Path
from app.actions.actionsInt import ActionsInt
from app.flow.flows import SellerFlow
from app.config.exceptions import IMGDoesntExistError


class SellerFlowImpl(SellerFlow):
    def __init__(
        self,
        actions:ActionsInt,
        path_to_vendendor:str,
        path_to_search:str,
    ):
        super().__init__(actions)

        path_vendendor = Path(path_to_vendendor)
        path_search = Path(path_to_search)

        if not (path_vendendor.exists() and path_vendendor.is_file()):
            raise IMGDoesntExistError(path_vendendor)
        if not (path_search.exists() and path_search.is_file()):
            raise IMGDoesntExistError(path_search)

        self.path_box_vendendor:str = path_to_vendendor
        self.path_to_search:str = path_to_search

    def _click_in_seller(self):
        seller_x, seller_y = self.actions.search(self.path_to_vendendor)

        modify_to_check:int = 30

        self.actions.left_click(
            seller_x+modify_to_check,
            seller_y,
        )
    

    def seller(self):
        self._click_in_seller()

        search_x, search_y = self.actions.search(self.path_to_search)
        self.actions.left_click(
            search_x,
            search_y,
        )

def getSellerFlowImpl(
    actions:ActionsInt,
    path_to_vendendor:str,
    path_to_search:str,
) -> SellerFlow:
    return SellerFlowImpl(
        actions=actions,
        path_to_vendendor=path_to_vendendor,
        path_to_search=path_to_search,
    )