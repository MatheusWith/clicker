from app.flow.flows import PaymentPlanFlow
from app.actions.actionsInt import ActionsInt


class PaymentPlanFlowImpl(PaymentPlanFlow):
    def __init__(
        self,
        actions:ActionsInt,
        path_to_plano_pagamento:str,
        path_to_search:str,
    ):
        super().__init__(actions)
        self._enshure_paths_exist([
            path_to_plano_pagamento,
            path_to_search
        ])
        self.path_to_plano_pagamento:str = path_to_plano_pagamento
        self.path_to_search:str = path_to_search


    def _click_in_plano_pagamento(self) -> None:
        plano_pagamento_x,plano_pagamento_y = self.actions.search(
            self.path_to_plano_pagamento
        )
        self.actions.left_click(
            plano_pagamento_x,
            plano_pagamento_y,
        )

    def payment_plan(self):
        self._click_in_plano_pagamento()

        search_x, search_y = self.actions.search(
            self.path_to_search
        )
        
        self.actions.left_click(search_x, search_y)

def getPlanoPagamentoFlowImpl(
    actions:ActionsInt,
    path_to_plano_pagamento:str,
    path_to_search:str,
) -> PaymentPlanFlow:
    return PaymentPlanFlowImpl(
        actions=actions,
        path_to_plano_pagamento=path_to_plano_pagamento,
        path_to_search=path_to_search,
    )