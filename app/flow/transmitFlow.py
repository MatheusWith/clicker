from app.flow.flows import TransmitFlow
from app.actions.actionsInt import ActionsInt

class TransmitFlowImpl(TransmitFlow):

    def __init__(
        self,
        actions:ActionsInt,
        path_to_transmitir:str,
    ):
        super().__init__(actions)
        self._enshure_paths_exist([
            path_to_transmitir
        ])

        self.path_to_transmitir:str = self.base_path + path_to_transmitir

    def execute(self):
        transmitir_x, transmitir_y = self.actions.search(
            self.path_to_transmitir
        )
        self.actions.left_click(
            transmitir_x,
            transmitir_y
        )

def getTransmitFlowImpl(
    actions:ActionsInt,
    path_to_transmitir:str,
) -> TransmitFlow:
    return TransmitFlowImpl(
        actions=actions,
        path_to_transmitir=path_to_transmitir,
    )
