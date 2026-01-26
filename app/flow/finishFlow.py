from app.flow.flows import FinishFlow
from app.actions.actionsInt import ActionsInt

class FinishFlowImpl(FinishFlow):
    def __init__(
        self,
        actions:ActionsInt,
        path_to_finish_label:str,
        path_to_ok_button:str,
    ):
        super().__init__(actions)
        self._enshure_paths_exist([
            path_to_finish_label,
            path_to_ok_button,
        ])
