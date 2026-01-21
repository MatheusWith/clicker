from pathlib import Path
from app.flow.flows import DocumentosFlow
from app.actions.actionsInt import ActionsInt
from app.config.exceptions import IMGDoesntExistError


class DocumentosFlowImpl(DocumentosFlow):
    def __init__(
        self,
        actions:ActionsInt,
        path_to_documento:str,
        path_to_data_inicial_label:str,
        path_to_data_final_label:str,
        path_to_search:str
    ):
        super().__init__(actions)
        path_documento = Path(path_to_documento)
        path_data_inicial_label = Path(path_to_data_final_label)
        path_data_final_label = Path(path_to_data_final_label)
        path_search = Path(path_to_search)

        if not (path_documento.exists() and path_documento.is_file()):
            raise IMGDoesntExistError(path_to_documento)
        if not (path_data_inicial_label.exists() and path_data_inicial_label.is_file()):
            raise IMGDoesntExistError(path_to_data_inicial_label)
        if not (path_data_final_label.exists() and path_data_final_label.is_file()):
            raise IMGDoesntExistError(path_to_data_final_label)
        if not (path_search.exists() and path_search.is_file()):
            raise IMGDoesntExistError(path_to_search)

        self.path_to_documento:str = path_to_documento
        self.path_to_data_inicial_label:str = path_to_data_inicial_label
        self.path_to_data_final_label:str = path_to_data_final_label
        self.path_to_search:str = path_to_search

    def _click_in_documento(self):
        doc_x, doc_y = self.actions.search(
            self.path_to_documento
        )
        self.actions.left_click(
            doc_x,
            doc_y,
        )

    def _write_data_inicial(self):
        ini_x, ini_y = self.actions.search(
            self.path_to_data_inicial_label
        )
        modify_to_field:int = 20 

        self.actions.left_click(
            ini_x + modify_to_field,
            ini_y,
        )

        self.actions.write("01012020")

    def _write_data_final(self):
        end_x, end_y = self.actions.search(
            self.path_to_data_final_label
        )
        modify_to_field:int = 20

        self.actions.left_click(
            end_x+modify_to_field,
            end_y,
        )

        self.actions.write("31122030")
        

    def documentos(self):
        self._click_in_documento()
        self._write_data_inicial()
        self._write_data_inicial()

        search_x,search_y = self.actions.search(
            self.path_to_search
        )

        self.actions.left_click(
            search_x,
            search_y
        )



