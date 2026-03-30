from app.flow.flows import FinishFlow
from app.actions.actionsInt import ActionsInt


class FinishFlowImpl(FinishFlow):
    def __init__(
        self,
        actions: ActionsInt,
        path_to_finish_label: str,
        path_to_yes_confirmation: str,
        path_to_ok_button: str,
        modify_to_field_finish_x: int,
        modify_to_field_finish_y: int,
    ):
        super().__init__(actions)
        self._enshure_paths_exist(
            [
                path_to_yes_confirmation,
                path_to_finish_label,
                path_to_ok_button,
            ]
        )
        self.path_to_yes_confirmation: str = self.base_path + path_to_yes_confirmation
        self.path_to_finish_label: str = self.base_path + path_to_finish_label
        self.path_to_ok_button: str = self.base_path + path_to_ok_button
        self.modify_to_field_finish_x: int = modify_to_field_finish_x
        self.modify_to_field_finish_y: int = modify_to_field_finish_y

    def _click_in_finish_label(self):
        finish_x, finish_y = self.actions.search(self.path_to_finish_label)
        self.actions.left_click(
            finish_x + self.modify_to_field_finish_x,
            finish_y + self.modify_to_field_finish_y,
        )

    def _confirmation(self):
        yes_x, yes_y = self.actions.search(self.path_to_yes_confirmation)
        self.actions.hot_key("enter")

    def _do_ok(self):
        ok_x, ok_y = self.actions.search(self.path_to_ok_button)
        self.actions.hot_key("enter")

    def execute(self):
        self._do_ok()
        self._click_in_finish_label()
        self._confirmation()


def getFinishFlowImpl(
    actions: ActionsInt,
    path_to_finish_label: str,
    path_to_yes_confirmation: str,
    path_to_ok_button: str,
    modify_to_field_finish_x: int,
    modify_to_field_finish_y: int,
) -> FinishFlow:
    return FinishFlowImpl(
        actions=actions,
        path_to_finish_label=path_to_finish_label,
        path_to_yes_confirmation=path_to_yes_confirmation,
        path_to_ok_button=path_to_ok_button,
        modify_to_field_finish_x=modify_to_field_finish_x,
        modify_to_field_finish_y=modify_to_field_finish_y,
    )
