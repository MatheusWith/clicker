from pathlib import Path
from app.actions.actionsInt import ActionsInt
from app.flow.flows import SellerFlow
from app.config.exceptions import IMGDoesntExistError


class SellerFlowImpl(SellerFlow):
    def __init__(
        self,
        actions:ActionsInt,
        path_to_box_vendendor:str,
        path_to_search:str,
    ):
        super().__init__(actions)

        path_box_vendendor = Path(path_to_box_vendendor)
        path_search = Path(path_to_search)

        if not (path_box_vendendor.exists() and path_box_vendendor.is_file()):
            raise IMGDoesntExistError(path_box_vendendor)
        if not (path_search.exists() and path_search.is_file()):
            raise IMGDoesntExistError(path_search)

        self.path_box_vendendor:str = path_to_box_vendendor
        self.path_to_search:str = path_to_search

    def _check_box_seller(self):
        box_seller_x, box_seller_y = self.actions.search(self.path_box_vendendor)

        modify_to_check:int = 30

        self.actions.left_click(
            box_seller_x+modify_to_check,
            box_seller_y,
        )
    

    def seller(self):
        self._check_box_seller()

        search_x, search_y = self.actions.search(self.path_to_search)
        self.actions.left_click(
            search_x,
            search_y,
        )
