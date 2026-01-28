from app.flow.flows import FinishFlow
from app.actions.actionsInt import ActionsInt

class FinishFlowImpl(FinishFlow):
    def __init__(
        self,
        actions:ActionsInt,
        path_to_finish_label:str,
        path_to_yes_confirmation:str,
        path_to_ok_button:str,
        path_to_finish_finish:str,
    ):
        super().__init__(actions)
        self._enshure_paths_exist([
            path_to_yes_confirmation,
            path_to_finish_label,
            path_to_ok_button,
            path_to_finish_finish,
        ])
        self.path_to_yes_confirmation = self.base_path + self.path_to_yes_confirmation
        self.path_to_finish_label:str = self.base_path + path_to_finish_label
        self.path_to_ok_button:str = self.base_path + path_to_ok_button
        self.path_to_finish_finish:str = self.base_path + path_to_finish_finish


    def _click_in_finish_label(self):
        finish_x, finish_y = self.actions.search(
            self.path_to_finish_label
        )

        self.actions.left_click(
            finish_x,
            finish_y,
        )

    def _confirmation(self):
        yes_x, yes_y = self.actions.search(
            self.path_to_yes_confirmation
        )

        self.actions.left_click(
            yes_x,
            yes_y,
        )

    def _finalization(self):
        finish_x,finish_y = self.actions.search(
            self.paht_to_finish_finish,
        )

        self.actions.left_click(
            finish_x,
            finish_y,
        )
        

    def execute(self):
        self._click_in_finish_label()
        self._confirmation()
        self._finalization()


def getFinishFlowImpl(
    actions:ActionsInt,
    path_to_finish_label:str,
    path_to_yes_confirmation:str,
    path_to_ok_button:str,
    path_to_finish_finish:str,
) -> FinishFlow:
    return FinishFlowImpl(
        actions=actions,
        path_to_finish_label=path_to_finish_label,
        path_to_yes_confirmation=path_to_yes_confirmation,
        path_to_ok_button=path_to_ok_button,
        path_to_finish_finish=path_to_finish_finish,
    )