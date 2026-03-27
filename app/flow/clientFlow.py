from app.flow.flows import ClientFlow
from app.actions.actionsInt import ActionsInt


class ClientFlowImpl(ClientFlow):
    def __init__(
        self,
        actions: ActionsInt,
        path_to_client: str,
        modify_to_field_x: int,
        modify_to_field_y: int,
    ):
        super().__init__(actions)
        self._enshure_paths_exist(
            [
                path_to_client,
            ]
        )

        self.path_to_client: str = self.base_path + path_to_client
        self.modify_to_field_x: int = modify_to_field_x
        self.modify_to_field_y: int = modify_to_field_y

    def _click_in_client(self) -> None:
        client_x, client_y = self.actions.search(self.path_to_client)
        self.actions.left_click(
            client_x + self.modify_to_field_x,
            client_y + self.modify_to_field_y,
        )

    def execute(self):
        self._click_in_client()
        self.actions.hot_key(
            "alt",
            "p",
        )


def getClientFlowImpl(
    actions: ActionsInt,
    path_to_client: str,
    modify_to_field_x: int,
    modify_to_field_y: int,
) -> ClientFlow:
    return ClientFlowImpl(
        actions=actions,
        path_to_client=path_to_client,
        modify_to_field_x=modify_to_field_x,
        modify_to_field_y=modify_to_field_y,
    )
