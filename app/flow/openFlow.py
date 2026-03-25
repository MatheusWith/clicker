from app.flow.flows import OpenFlow
from app.actions.actionsInt import ActionsInt


class OpenFlowImpl(OpenFlow):
    def __init__(
        self,
        actions: ActionsInt,
        modify_to_field_x: int,
        modify_to_field_y: int,
        path_to_app_label: str,
    ):
        super().__init__(actions=actions)
        self._enshure_paths_exist(
            [
                path_to_app_label,
            ]
        )
        self.path_to_app_label = self.base_path + path_to_app_label
        self.modify_to_field_x: int = modify_to_field_x
        self.modify_to_field_y: int = modify_to_field_y

    def execute(self):
        app_x, app_y = self.actions.search(self.path_to_app_label)
        self.actions.left_click(
            app_x + self.modify_to_field_x,
            app_y + self.modify_to_field_y,
            2,
        )


def getOpenFlowImpl(
    actions: ActionsInt,
    path_to_app_label: str,
    modify_to_field_x: int,
    modify_to_field_y: int,
) -> OpenFlow:
    return OpenFlowImpl(
        actions=actions,
        modify_to_field_x=modify_to_field_x,
        modify_to_field_y=modify_to_field_y,
        path_to_app_label=path_to_app_label,
    )
