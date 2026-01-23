from pathlib import Path
from app.flow.flows import PaymentPlanFlow
from app.actions.actionsInt import ActionsInt
from app.config.exceptions import IMGDoesntExistError


class PaymentPlanFlowImpl(PaymentPlanFlow):
    def __init__(
        self,
        actions:ActionsInt,
        path_to_plano_pagamento:str,
        path_to_search:str,
    ):
        super().__init__(actions)

        path_plano_pagamento = Path(path_to_plano_pagamento)
        path_search = Path(path_to_search)

        if not(path_plano_pagamento.exists() and path_plano_pagamento.is_file()):
            raise IMGDoesntExistError(path_to_plano_pagamento)
        if not (path_search.exists() and path_search.is_file()):
            raise IMGDoesntExistError(path_to_search)

    def _click_in_plano_pagamento(self):
        plano_pagamento_x,plano_pagamento_y = self.actions.search(
            self.path_to_plano_pagamento
        )
        self.actions.left_click(
            plano_pagamento_x,
            plano_pagamento_y,
        )

    def plano_pagamento(self):
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