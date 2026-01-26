from app.config.setup import configure
from app.config.config import settings
from app.actions.actionsInt import ActionsInt
from app.actions.actionsPyAutoGui import getActionPyAutoGUIImpl
from app.flow.flows import LoginFlow
from app.flow.loginFlow import getLoginFlowImpl


def main():
    configure(settings=settings)

    actions:ActionsInt = getActionPyAutoGUIImpl()

    login_flows: LoginFlow = getLoginFlowImpl(
        actions=actions,
        path_to_username="login_flow/username_label.png",
        path_to_password="login_flow/password_label.png",
        path_to_login="login_flow/login_button.png",
    )

    login_flows.login()


if __name__ == "__main__":
    main()