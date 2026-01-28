from app.flow.flows import ProductFlow
from app.actions.actionsInt import ActionsInt


class ProductFlowImpl(ProductFlow):
    def __init__(
        self,
        actions:ActionsInt,
        path_to_produto:str,
        path_to_box_table:str,
        path_to_box_produto_saldo:str,
        path_to_search:str,
    ):
        super().__init__(actions)
        self._enshure_paths_exist([
            path_to_produto,
            path_to_box_table,
            path_to_box_produto_saldo,
            path_to_search,
        ])

        self.path_to_produto:str = self.base_path + path_to_produto
        self.path_to_box_table:str = self.base_path + path_to_box_table
        self.path_to_box_produto_saldo:str = self.base_path + path_to_box_produto_saldo
        self.path_to_search:str = self.base_path + path_to_search

    def _click_in_product(self) -> None:
        product_x, product_y = self.actions.search(self.path_to_produto)
        self.actions.left_click(
            product_x,
            product_y,
        )

    def _check_tabela_prazo(self) -> None:
        check_box_x, check_box_y = self.actions.search(
            self.path_to_box_table
        )
        modify_to_check:int = -60
        
        self.actions.left_click(
            check_box_x+modify_to_check,
            check_box_y,
        )

    def _uncheck_saldo_estoque(self) -> None:
        check_box_x, check_box_y = self.actions.search(
            self.path_to_box_produto_saldo,
        )

        self.actions.left_click(
            check_box_x,
            check_box_y,
        )

    def execute(self):
        self._click_in_product()
        self._check_tabela_prazo()
        self._uncheck_saldo_estoque()

        search_x, search_y = self.actions.search(
            self.path_to_search
        )
        
        self.actions.left_click(search_x, search_y)


def getProductFlowImpl(
    actions:ActionsInt,
    path_to_produto:str,
    path_to_box_table:str,
    path_to_box_produto_saldo:str,
    path_to_search:str,
) -> ProductFlow:
    return ProductFlowImpl(
        actions=actions,
        path_to_produto=path_to_produto,
        path_to_box_table=path_to_box_table,
        path_to_box_produto_saldo=path_to_box_produto_saldo,
        path_to_search=path_to_search,
    )