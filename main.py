from app.config.setup import configure
from app.config.config import settings

from app.automation.automationTransmit import getTransmitAutomationImpl, TransmitSchema
from app.automation.automationInt import AutomationInt


def main():
    configure(settings=settings)
    transmit_schema: TransmitSchema = TransmitSchema(
        login=settings.LOGIN,
        password=settings.PASSWORD,
        start_date=settings.START_DATE,
        end_date=settings.END_DATE,
        mtf_login_x=settings.MTF_LOGIN_X,
        mtf_login_y=settings.MTF_LOGIN_Y,
        mtf_seller=settings.MTF_SELLER,
        mtf_product_deadtable=settings.MTF_PRODUCT_DEADTABLE,
        mtf_product_stock_balance=settings.MTF_PRODUCT_STOCK_BALANCE,
        mtf_document_open_doc_x=settings.MTF_DOCUMENT_OPEN_DOC_X,
        mtf_document_open_doc_y=settings.MTF_DOCUMENT_OPEN_DOC_Y,
        mtf_document_date_init_x=settings.MTF_DOCUMENT_DATE_INIT_X,
        mtf_document_date_init_y=settings.MTF_DOCUMENT_DATE_INIT_Y,
        mtf_document_date_end_x=settings.MTF_DOCUMENT_DATE_END_X,
        mtf_document_date_end_y=settings.MTF_DOCUMENT_DATE_END_Y,
        mtf_open_x=settings.MTF_OPEN_X,
        mtf_open_y=settings.MTF_OPEN_Y,
    )
    transmitAutomation: AutomationInt = getTransmitAutomationImpl(
        transmit=transmit_schema
    )
    transmitAutomation.run()


if __name__ == "__main__":
    main()
