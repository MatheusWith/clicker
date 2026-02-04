from app.flow.flows import DocumentFlow
from app.actions.actionsInt import ActionsInt
from app.config.exceptions import EndDateSettinsIsNoneError, StartDateSettinsIsNoneError
from app.config.config import settings


class DocumentFlowImpl(DocumentFlow):
    def __init__(
        self,
        actions:ActionsInt,
        path_to_documento:str,
        path_to_data_inicial_label:str,
        path_to_data_final_label:str,
        path_to_document_type_label:str,
        path_to_boleto:str
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
            path_to_document_type_label,
            path_to_boleto,
        ])

        self.path_to_documento:str = self.base_path + path_to_documento
        self.path_to_data_inicial_label:str = self.base_path + path_to_data_inicial_label
        self.path_to_data_final_label:str = self.base_path + path_to_data_final_label
        self.path_to_document_type_label:str = self.base_path + path_to_document_type_label
        self.path_to_boleto:str = self.base_path + path_to_boleto

        self.start_date:str = settings.START_DATE
        self.end_date:str = settings.END_DATE

    def _open_doc_type(self) -> None:
        doc_type_label_x, doc_type_label_y = self.actions.search(
            self.path_to_document_type_label
        )
        modify_to_field_x:int = 55
        modify_to_field_y:int = 25
        self.actions.left_click(
            doc_type_label_x + modify_to_field_x,
            doc_type_label_y + modify_to_field_y,
        )

    def _select_doc_type(self) -> None: 
        boleto_x, boleto_y = self.actions.search(
            self.path_to_boleto
        )
        self.actions.left_click(
            boleto_x,
            boleto_y,
            clicks=2,
        )

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
        modify_to_field_x:int = -20 
        modify_to_field_y:int = 25

        self.actions.left_click(
            ini_x + modify_to_field_x,
            ini_y + modify_to_field_y,
            clicks=2,
        )

        self.actions.write(self.start_date)

    def _write_data_final(self) -> None:
        end_x, end_y = self.actions.search(
            self.path_to_data_final_label
        )
        modify_to_field_x:int = 50
        modify_to_field_y:int = 25

        self.actions.left_click(
            end_x+modify_to_field_x,
            end_y+modify_to_field_y,
            clicks=2,
        )

        self.actions.write(self.end_date)
        
    def execute(self):
        self._click_in_documento()
        self._write_data_inicial()
        self._write_data_final()
        self._open_doc_type()
        self._select_doc_type()

        self.actions.left_click(
            'alt',
            'p',
        )


def getDocumentFlowImpl(
    actions:ActionsInt,
    path_to_documento:str,
    path_to_data_inicial_label:str,
    path_to_data_final_label:str,
    path_to_document_type_label:str,
    path_to_boleto:str,
) -> DocumentFlow:
    return DocumentFlowImpl(
        actions=actions,
        path_to_documento=path_to_documento,
        path_to_data_inicial_label=path_to_data_inicial_label,
        path_to_data_final_label=path_to_data_final_label,
        path_to_document_type_label=path_to_document_type_label,
        path_to_boleto=path_to_boleto,
    )


