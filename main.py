from app.config.setup import configure
from app.config.config import settings

from app.automation.automationTransmit import getTransmitAutomationImpl
from app.automation.automationInt import AutomationInt


def main():
    configure(settings=settings)
    
    transmitAutomation: AutomationInt = getTransmitAutomationImpl()
    transmitAutomation.run()
    

if __name__ == "__main__":
    main()