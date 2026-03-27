from app.flow.flows import PaymentPlanFlow
from app.actions.actionsInt import ActionsInt


class PaymentPlanFlowImpl(PaymentPlanFlow):
    def __init__(
        self,
        actions: ActionsInt,
        path_to_plano_pagamento: str,
        modify_to_field_x: int,
        modify_to_field_y: int,
    ):
        super().__init__(actions)
        self._enshure_paths_exist(
            [
                path_to_plano_pagamento,
            ]
        )
        self.path_to_plano_pagamento: str = self.base_path + path_to_plano_pagamento
        self.modify_to_field_x: int = modify_to_field_x
        self.modify_to_field_y: int = modify_to_field_y

    def _click_in_plano_pagamento(self) -> None:
        plano_pagamento_x, plano_pagamento_y = self.actions.search(
            self.path_to_plano_pagamento
        )
        self.actions.left_click(
            plano_pagamento_x + self.modify_to_field_x,
            plano_pagamento_y + self.modify_to_field_y,
        )

    def execute(self):
        self._click_in_plano_pagamento()

        self.actions.hot_key(
            "alt",
            "p",
        )


def getPaymentPlanFlowImpl(
    actions: ActionsInt,
    path_to_plano_pagamento: str,
    modify_to_field_x: int,
    modify_to_field_y: int,
) -> PaymentPlanFlow:
    return PaymentPlanFlowImpl(
        actions=actions,
        path_to_plano_pagamento=path_to_plano_pagamento,
        modify_to_field_x=modify_to_field_x,
        modify_to_field_y=modify_to_field_y,
    )
