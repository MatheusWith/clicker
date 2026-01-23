from pathlib import Path
from app.flow.flows import ClientFlow
from app.actions.actionsInt import ActionsInt
from app.config.exceptions import IMGDoesntExistError


class ClientFlowImpl(ClientFlow):
    def __init__(
        self,
        actions:ActionsInt,
        path_to_client:str,
        path_to_search:str,
    ):
        super().__init__(actions)
        self._enshure_paths_exist([
            path_to_client,
            path_to_search
        ])

        self.path_to_client:str = path_to_client
        self.path_to_search:str = path_to_search


    def _click_in_client(self):
        client_x, client_y = self.actions.search(
            self.path_to_client
        )
        self.left_click(
            client_x,
            client_y,
        )

    def client(self):
        self._click_in_client()
        search_x, search_y = self.actions.search(
            self.path_to_search
        )
        
        self.actions.left_click(search_x, search_y)


def getClientFlowImpl(
    actions:ActionsInt,
    path_to_client:str,
    path_to_search:str,
) -> ClientFlow:
    return ClientFlowImpl(
        actions=actions,
        path_to_client=path_to_client,
        path_to_search=path_to_search,
    )



