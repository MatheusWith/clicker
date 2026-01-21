from pathlib import Path
from app.flow.flows import DocumentosFlow
from app.actions.actionsInt import ActionsInt
from app.config.exceptions import IMGDoesntExistError
from app.config.exceptions import EndDateSettinsIsNoneError, StartDateSettinsIsNoneError
from app.config.config import settings


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

        if settings.START_DATE is None:
            raise StartDateSettinsIsNoneError
        if settings.END_DATE is None:
            raise EndDateSettinsIsNoneError

        self.start_date = settings.START_DATE
        self.end_date = settings.END_DATE

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

        self.actions.write(self.start_date)

    def _write_data_final(self):
        end_x, end_y = self.actions.search(
            self.path_to_data_final_label
        )
        modify_to_field:int = 20

        self.actions.left_click(
            end_x+modify_to_field,
            end_y,
        )

        self.actions.write(self.end_date)
        
    def documentos(self):
        self._click_in_documento()
        self._write_data_inicial()
        self._write_data_final()

        search_x,search_y = self.actions.search(
            self.path_to_search
        )

        self.actions.left_click(
            search_x,
            search_y,
        )


def getDocumentosFlowImpl(
    actions:ActionsInt,
    path_to_documento:str,
    path_to_data_inicial_label:str,
    path_to_data_final_label:str,
    path_to_search:str,
) -> DocumentosFlow:
    return DocumentosFlowImpl(
        actions=actions,
        path_to_documento=path_to_documento,
        path_to_data_inicial_label=path_to_data_inicial_label,
        path_to_data_final_label=path_to_data_final_label,
        path_to_search=path_to_search,
    )


