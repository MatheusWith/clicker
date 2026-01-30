import time
from app.config.setup import configure
from app.config.config import settings
from app.actions.actionsInt import ActionsInt
from app.flow.flows import FlowInt
from app.actions.actionsPyAutoGui import getActionPyAutoGUIImpl
from app.flow.flows import (
    OpenFlow,
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
from app.flow.openFlow import getOpenFlowImpl

from app.automation.automationTransmit import getTransmitAutomationImpl
from app.automation.automationInt import AutomationInt


def main():
    configure(settings=settings)
    
    transmitAutomation: AutomationInt = getTransmitAutomationImpl()
    transmitAutomation.run()
    

if __name__ == "__main__":
    main()