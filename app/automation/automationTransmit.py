import time
from app.automation.automationInt import AutomationInt
from app.actions.actionsInt import ActionsInt
from app.flow.flows import FlowInt
from app.flow.flows import TransmitFlow
from app.flow.loginFlow import getLoginFlowImpl
from app.flow.sellerFlow import getSellerFlowImpl
from app.flow.productFlow import getProductFlowImpl
from app.flow.clientFlow import getClientFlowImpl
from app.flow.paymentPlanFlow import getPaymentPlanFlowImpl
from app.flow.documentFlow import getDocumentFlowImpl
from app.flow.transmitFlow import getTransmitFlowImpl
from app.flow.finishFlow import getFinishFlowImpl
from app.flow.openFlow import getOpenFlowImpl
from app.actions.actionsPyAutoGui import getActionPyAutoGUIImpl
from pydantic import BaseModel


class TransmitSchema(BaseModel):
    login: str
    password: str
    start_date: str
    end_date: str
    mtf_login_x: int
    mtf_login_y: int
    mtf_seller: int
    mtf_product_deadtable: int
    mtf_product_stock_balance: int
    mtf_document_open_doc_x: int
    mtf_document_open_doc_y: int
    mtf_document_date_init_x: int
    mtf_document_date_init_y: int
    mtf_document_date_end_x: int
    mtf_document_date_end_y: int
    mtf_open_x: int
    mtf_open_y: int


class TransmitAutomationImpl(AutomationInt):
    def __init__(self, transmit: TransmitSchema):
        self.transmit: TransmitSchema = transmit
        self.actions: ActionsInt = getActionPyAutoGUIImpl()

        self.flows: list[FlowInt] = self.get_flows()

    def get_flows(self) -> list[FlowInt]:
        return [
            getOpenFlowImpl(
                actions=self.actions,
                modify_to_field_x=self.transmit.mtf_open_x,
                modify_to_field_y=self.transmit.mtf_open_y,
                path_to_app_label="open_flow/app_label.png",
            ),
            getLoginFlowImpl(
                actions=self.actions,
                path_to_username="login_flow/username_label.png",
                path_to_password="login_flow/password_label.png",
                path_to_login="login_flow/login_button.png",
                username=self.transmit.login,
                password=self.transmit.password,
                modify_to_field_x=self.transmit.mtf_login_x,
                modify_to_field_y=self.transmit.mtf_login_y,
            ),
            getSellerFlowImpl(
                actions=self.actions,
                path_to_vendendor="vendendor_flow/vendendor_label.png",
                modify_to_check=self.transmit.mtf_seller,
            ),
            getProductFlowImpl(
                actions=self.actions,
                path_to_produto="product_flow/product_label.png",
                path_to_box_produto_saldo="product_flow/product_saldo.png",
                path_to_box_table="product_flow/deadline_table.png",
                modify_to_check_stock_balance=self.transmit.mtf_product_stock_balance,
                modify_to_check_deadtable=self.transmit.mtf_product_deadtable,
            ),
            getClientFlowImpl(
                actions=self.actions,
                path_to_client="client_flow/client_label.png",
            ),
            getPaymentPlanFlowImpl(
                actions=self.actions,
                path_to_plano_pagamento="plano_pagamento_flow/plano_pagamento_label.png",
            ),
            getDocumentFlowImpl(
                actions=self.actions,
                path_to_documento="document_flow/document_label.png",
                path_to_data_inicial_label="document_flow/inital_date_label.png",
                path_to_data_final_label="document_flow/inital_date_label.png",
                path_to_document_type_label="document_flow/document_type_label.png",
                path_to_boleto="document_flow/boleto.png",
                start_date=self.transmit.start_date,
                end_date=self.transmit.end_date,
                modify_to_field_open_doc_x=self.transmit.mtf_document_open_doc_x,
                modify_to_field_open_doc_y=self.transmit.mtf_document_open_doc_y,
                modify_to_field_date_init_x=self.transmit.mtf_document_date_init_x,
                modify_to_field_date_init_y=self.transmit.mtf_document_date_init_y,
                modify_to_field_date_end_x=self.transmit.mtf_document_date_end_x,
                modify_to_field_date_end_y=self.transmit.mtf_document_date_end_y,
            ),
            getTransmitFlowImpl(
                actions=self.actions,
                path_to_transmitir="transmit_flow/transmit_button.png",
            ),
            getFinishFlowImpl(
                actions=self.actions,
                path_to_finish_label="finish_flow/finish_label.png",
                path_to_yes_confirmation="finish_flow/yes_confirmation.png",
                path_to_ok_button="finish_flow/ok_button.png",
            ),
        ]

    def run(self):
        for f in self.flows:
            f.execute()
            if isinstance(f, TransmitFlow):
                time.sleep(120)
            else:
                time.sleep(10)


def getTransmitAutomationImpl(
    transmit: TransmitSchema,
) -> TransmitAutomationImpl:
    return TransmitAutomationImpl(transmit=transmit)
