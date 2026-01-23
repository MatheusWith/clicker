from pathlib import Path
from app.flow.flows import ProductFlow
from app.actions.actionsInt import ActionsInt
from app.config.exceptions import IMGDoesntExistError


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

        path_produto = Path(path_to_produto)
        path_box_table = Path(path_to_box_table)
        path_produto_saldo = Path(path_to_box_produto_saldo)
        path_search = Path(path_to_search)

        if not (path_produto.exists() and path_produto.is_file()):
            raise IMGDoesntExistError(path_produto)
        if not (path_box_table.exists() and path_box_table.is_file()):
            raise IMGDoesntExistError(path_box_table)
        if not (path_produto_saldo.exists() and path_produto_saldo.is_file()):
            raise IMGDoesntExistError(path_produto_saldo)
        if not (path_search.exists() and path_search.is_file()):
            raise IMGDoesntExistError(path_search)

        self.path_to_produto = path_to_produto
        self.path_to_box_table = path_to_box_table
        self.path_to_box_produto_saldo = path_to_box_produto_saldo
        self.path_to_search = path_to_search

    def _click_in_product(self):
        product_x, product_y = self.actions.search(self.path_to_produto)
        self.actions.left_click(
            product_x,
            product_y,
        )

    def _check_tabela_prazo(self):
        check_box_x, check_box_y = self.actions.search(
            self.path_to_box_table
        )
        modify_to_check:int = 20
        
        self.actions.left_click(
            check_box_x+modify_to_check,
            check_box_y,
        )

    def _uncheck_saldo_estoque(self):
        check_box_x, check_box_y = self.actions.search(
            self.path_to_box_produto_saldo,
        )
        modify_to_check: int = 20

        self.actions.left_click(
            check_box_x,
            check_box_y,
        )

    def product(self):
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