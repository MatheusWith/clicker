from app.flow.flows import ProductFlow
from app.actions.actionsInt import ActionsInt


class ProductFlowImpl(ProductFlow):
    def __init__(
        self,
        actions:ActionsInt,
        path_to_produto:str,
        path_to_box_table:str,
        path_to_box_produto_saldo:str,
        modify_to_check_deadtable:int,
        modify_to_check_stock_balance:int,
    ):
        super().__init__(actions)
        self._enshure_paths_exist([
            path_to_produto,
            path_to_box_table,
            path_to_box_produto_saldo,
        ])

        self.modify_to_check_deadtable:int = modify_to_check_deadtable
        self.modify_to_check_stock_balance:int = modify_to_check_stock_balance
        self.path_to_produto:str = self.base_path + path_to_produto
        self.path_to_box_table:str = self.base_path + path_to_box_table
        self.path_to_box_produto_saldo:str = self.base_path + path_to_box_produto_saldo

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
        
        self.actions.left_click(
            check_box_x+self.modify_to_check_deadtable,
            check_box_y,
        )

    def _uncheck_saldo_estoque(self) -> None:
        check_box_x, check_box_y = self.actions.search(
            self.path_to_box_produto_saldo,
        )

        self.actions.left_click(
            check_box_x,
            check_box_y-self.modify_to_check_stock_balance,
        )

    def execute(self):
        self._click_in_product()
        self._check_tabela_prazo()
        self._uncheck_saldo_estoque()
        self.actions.hot_key(
            'alt',
            'p',
        )

def getProductFlowImpl(
    actions:ActionsInt,
    path_to_produto:str,
    path_to_box_table:str,
    path_to_box_produto_saldo:str,
    modify_to_check_stock_balance:int,
    modify_to_check_deadtable=int,
) -> ProductFlow:
    return ProductFlowImpl(
        actions=actions,
        path_to_produto=path_to_produto,
        path_to_box_table=path_to_box_table,
        path_to_box_produto_saldo=path_to_box_produto_saldo,
        modify_to_check_stock_balance=modify_to_check_stock_balance,
        modify_to_check_deadtable=modify_to_check_deadtable,
    )