from app.config.setup import configure
from app.config.config import settings
<<<<<<< Updated upstream
=======
from app.actions.actionsInt import ActionsInt
from app.actions.actionsPyAutoGui import getActionPyAutoGUIImpl
from app.flow.flows import LoginFlow
from app.flow.loginFlow import getLoginFlowImpl
>>>>>>> Stashed changes


def main():
    configure(settings=settings)

<<<<<<< Updated upstream
=======
    actions:ActionsInt = getActionPyAutoGUIImpl()

    login_flows: LoginFlow = getLoginFlowImpl(
        actions=actions,
        path_to_username="app/img/login_flow/username_label.png",
        path_to_password="app/img/login_flow/password_label.png",
        path_to_login="app/img/login_flow/login_button.png",
    )

    login_flows.login()

>>>>>>> Stashed changes

if __name__ == "__main__":
    main()
