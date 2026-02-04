from app.flow.flows import ClientFlow
from app.actions.actionsInt import ActionsInt


class ClientFlowImpl(ClientFlow):
    def __init__(
        self,
        actions:ActionsInt,
        path_to_client:str,
    ):
        super().__init__(actions)
        self._enshure_paths_exist([
            path_to_client,
        ])

        self.path_to_client:str = self.base_path + path_to_client


    def _click_in_client(self) -> None:
        client_x, client_y = self.actions.search(
            self.path_to_client
        )
        self.actions.left_click(
            client_x,
            client_y,
        )

    def execute(self):
        self._click_in_client()
        self.actions.hot_key(
            'alt',
            'p',
        )


def getClientFlowImpl(
    actions:ActionsInt,
    path_to_client:str,
) -> ClientFlow:
    return ClientFlowImpl(
        actions=actions,
        path_to_client=path_to_client,
    )



