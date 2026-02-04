from app.actions.actionsInt import ActionsInt
from app.flow.flows import SellerFlow


class SellerFlowImpl(SellerFlow):
    def __init__(
        self,
        actions:ActionsInt,
        path_to_vendendor:str,
        modify_to_check:int,
    ):
        super().__init__(actions)
        self._enshure_paths_exist([
            path_to_vendendor,
        ])

        self.modify_to_check:int = modify_to_check
        self.path_to_vendendor:str = self.base_path + path_to_vendendor

    def _click_in_seller(self) -> None:
        seller_x, seller_y = self.actions.search(self.path_to_vendendor)

        self.actions.left_click(
            seller_x+self.modify_to_check,
            seller_y,
        )

    def execute(self):
        self._click_in_seller()

        self.actions.hot_key(
            'alt',
            'p',
        )

def getSellerFlowImpl(
    actions:ActionsInt,
    path_to_vendendor:str,
    modify_to_check:int,
) -> SellerFlow:
    return SellerFlowImpl(
        actions=actions,
        path_to_vendendor=path_to_vendendor,
        modify_to_check=modify_to_check,
    )