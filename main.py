from app.config.setup import configure
from app.config.config import settings

from app.automation.automationTransmit import getTransmitAutomationImpl, TransmitSchema
from app.automation.automationInt import AutomationInt


def main():
    configure(settings=settings)
    schema: TransmitSchema = TransmitSchema(settings)
    transmitAutomation: AutomationInt = getTransmitAutomationImpl(transmit=schema)
    transmitAutomation.run()


if __name__ == "__main__":
    main()
