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
from app.config.config import settings
from app.config.exceptions import LoginSettinsIsNoneError
from app.config.exceptions import PasswordSettinsIsNoneError
from app.config.exceptions import EndDateSettinsIsNoneError, StartDateSettinsIsNoneError



class TransmitAutomationImpl(AutomationInt):
    def __init__(self):
        if settings.LOGIN is None:
            raise LoginSettinsIsNoneError
        if settings.PASSWORD is None:
            raise PasswordSettinsIsNoneError

        if settings.START_DATE is None:
            raise StartDateSettinsIsNoneError
        if settings.END_DATE is None:
            raise EndDateSettinsIsNoneError

        if settings.MTF_LOGIN:
            raise ValueError("nao tem o modificador ate o campo")
        if settings.MTF_SELLER:
            raise ValueError("Nao tem o modificador seller")

        self.actions:ActionsInt = getActionPyAutoGUIImpl()

        self.flows: list[FlowInt] = [
            getOpenFlowImpl(
                actions=self.actions,
                path_to_app_label="open_flow/app_label.png"
            ),
            getLoginFlowImpl(
                actions=self.actions,
                path_to_username="login_flow/username_label.png",
                path_to_password="login_flow/password_label.png",
                path_to_login="login_flow/login_button.png",
                username=settings.LOGIN,
                password=settings.PASSWORD,
                modify_to_field=settings.MTF_LOGIN,
            ),
            getSellerFlowImpl(
                actions=self.actions,
                path_to_vendendor="vendendor_flow/vendendor_label.png",
                modify_to_check=settings.MTF_SELLER,
            ),
            getProductFlowImpl(
                actions=self.actions,
                path_to_produto="product_flow/product_label.png",
                path_to_box_produto_saldo="product_flow/product_saldo.png",
                path_to_box_table="product_flow/deadline_table.png",
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
            if isinstance(f,TransmitFlow):
                time.sleep(120)
            else:
                time.sleep(10)


def getTransmitAutomationImpl() -> TransmitAutomationImpl:
    return TransmitAutomationImpl()
