from app.config.setup import configure
from app.config.config import settings
from app.actions.actionsInt import ActionsInt
from app.flow.flows import FlowInt
from app.actions.actionsPyAutoGui import getActionPyAutoGUIImpl
from app.flow.flows import (
    LoginFlow, 
    SellerFlow,
    ProductFlow,
    ClientFlow,
    PaymentPlanFlow,
    DocumentFlow,
    TransmitFlow,
    FinishFlow,
)
from app.flow.loginFlow import getLoginFlowImpl
from app.flow.sellerFlow import getSellerFlowImpl
from app.flow.productFlow import getProductFlowImpl
from app.flow.clientFlow import getClientFlowImpl
from app.flow.paymentPlanFlow import getPaymentPlanFlowImpl
from app.flow.documentFlow import getDocumentFlowImpl
from app.flow.transmitFlow import getTransmitFlowImpl
from app.flow.finishFlow import getFinishFlowImpl
import time


def main():
    configure(settings=settings)

    actions:ActionsInt = getActionPyAutoGUIImpl()

    login_flow: LoginFlow = getLoginFlowImpl(
        actions=actions,
        path_to_username="login_flow/username_label.png",
        path_to_password="login_flow/password_label.png",
        path_to_login="login_flow/login_button.png",
    )
    seller_flow: SellerFlow = getSellerFlowImpl(
        actions=actions,
        path_to_vendendor="vendendor_flow/vendendor_label.png",
        path_to_search="search_button.png",
    )
    product_flow: ProductFlow = getProductFlowImpl(
        actions=actions,
        path_to_produto="product_flow/product_label.png",
        path_to_box_produto_saldo="product_flow/product_saldo.png",
        path_to_box_table="product_flow/deadline_table.png",
        path_to_search="search_button.png",
    )
    client_flow: ClientFlow = getClientFlowImpl(
        actions=actions,
        path_to_client="client_flow/client_label.png",
        path_to_search="search_button.png",
    )
    payment_plan_flow: PaymentPlanFlow = getPaymentPlanFlowImpl(
        actions=actions,
        path_to_plano_pagamento="plano_pagamento_flow/plano_pagamento_label.png",
        path_to_search="search_button.png",
    )
    document_flow: DocumentFlow = getDocumentFlowImpl(
        actions=actions,
        path_to_documento="document_flow/document_label.png",
        path_to_data_inicial_label="document_flow/inital_date_label.png",
        path_to_data_final_label="document_flow/inital_date_label.png",
        path_to_search="search_button.png",
    )
    transmit_flow: TransmitFlow = getTransmitFlowImpl(
        actions=actions,
        path_to_transmitir="transmit_flow/transmit_button.png",
    )
    finish_flow: FinishFlow = getFinishFlowImpl(
        actions=actions,
        path_to_finish_label="finish_flow/finish_label.png",
        path_to_yes_confirmation="finish_flow/yes_confirmation.png",
        path_to_ok_button="finish_flow/ok_button.png",
    )

    flows: list[FlowInt] = [
        login_flow,
        seller_flow,
        product_flow,
        client_flow,
        payment_plan_flow,
        document_flow,
        transmit_flow,
        finish_flow,
    ]

    for f in flows:
        f.execute()
        if isinstance(f,TransmitFlow):
            time.sleep(120)
        else:
            time.sleep(10)


if __name__ == "__main__":
    main()