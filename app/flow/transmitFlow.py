from app.flow.flows import TransmitFlow
from app.actions.actionsInt import ActionsInt


class TransmitFlowImpl(TransmitFlow):
    def __init__(
        self,
        actions: ActionsInt,
        path_to_transmitir: str,
        modify_to_field_x: int,
        modify_to_field_y: int,
    ):
        super().__init__(actions)
        self._enshure_paths_exist([path_to_transmitir])

        self.path_to_transmitir: str = self.base_path + path_to_transmitir
        self.modify_to_field_x: int = modify_to_field_x
        self.modify_to_field_y: int = modify_to_field_y

    def execute(self):
        transmitir_x, transmitir_y = self.actions.search(self.path_to_transmitir)
        self.actions.left_click(
            transmitir_x + self.modify_to_field_x,
            transmitir_y + self.modify_to_field_y,
        )


def getTransmitFlowImpl(
    actions: ActionsInt,
    path_to_transmitir: str,
    modify_to_field_x: int,
    modify_to_field_y: int,
) -> TransmitFlow:
    return TransmitFlowImpl(
        actions=actions,
        path_to_transmitir=path_to_transmitir,
        modify_to_field_x=modify_to_field_x,
        modify_to_field_y=modify_to_field_y,
    )
