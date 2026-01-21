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
        path_client = Path(path_to_client)
        path_search = Path(path_to_search)

        if not(path_client.exists() and path_client.is_file()):
            raise IMGDoesntExistError(path_to_client)
        if not (path_search.exists() and path_search.is_file()):
            raise IMGDoesntExistError(path_to_search)

        self.path_to_client = path_to_client
        self.path_to_search = path_to_search


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


