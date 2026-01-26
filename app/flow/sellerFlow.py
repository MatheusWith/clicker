from app.actions.actionsInt import ActionsInt
from app.flow.flows import SellerFlow


class SellerFlowImpl(SellerFlow):
    def __init__(
        self,
        actions:ActionsInt,
        path_to_vendendor:str,
        path_to_search:str,
    ):
        super().__init__(actions)
        self._enshure_paths_exist([
            path_to_vendendor,
            path_to_search,
        ])

        self.path_to_vendendor:str = self.base_path + path_to_vendendor
        self.path_to_search:str = self.base_path + path_to_search

    def _click_in_seller(self) -> None:
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