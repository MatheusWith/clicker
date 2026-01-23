from pathlib import Path
from app.flow.flows import DocumentFlow
from app.actions.actionsInt import ActionsInt
from app.config.exceptions import IMGDoesntExistError
from app.config.exceptions import EndDateSettinsIsNoneError, StartDateSettinsIsNoneError
from app.config.config import settings


class DocumentFlowImpl(DocumentFlow):
    def __init__(
        self,
        actions:ActionsInt,
        path_to_documento:str,
        path_to_data_inicial_label:str,
        path_to_data_final_label:str,
        path_to_search:str
    ):
        if settings.START_DATE is None:
            raise StartDateSettinsIsNoneError
        if settings.END_DATE is None:
            raise EndDateSettinsIsNoneError

        super().__init__(actions)
        self._enshure_paths_exist([
            path_to_documento,
            path_to_data_inicial_label,
            path_to_data_final_label,
            path_to_search
        ])

        self.path_to_documento:str = path_to_documento
        self.path_to_data_inicial_label:str = path_to_data_inicial_label
        self.path_to_data_final_label:str = path_to_data_final_label
        self.path_to_search:str = path_to_search

        self.start_date:str = settings.START_DATE
        self.end_date:str = settings.END_DATE

    def _click_in_documento(self) -> None:
        doc_x, doc_y = self.actions.search(
            self.path_to_documento
        )
        self.actions.left_click(
            doc_x,
            doc_y,
        )

    def _write_data_inicial(self) -> None:
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
        
    def document(self):
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


def getDocumentFlowImpl(
    actions:ActionsInt,
    path_to_documento:str,
    path_to_data_inicial_label:str,
    path_to_data_final_label:str,
    path_to_search:str,
) -> DocumentFlow:
    return DocumentFlowImpl(
        actions=actions,
        path_to_documento=path_to_documento,
        path_to_data_inicial_label=path_to_data_inicial_label,
        path_to_data_final_label=path_to_data_final_label,
        path_to_search=path_to_search,
    )


