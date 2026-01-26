from app.flow.flows import LoginFlow
from app.actions.actionsInt import ActionsInt
from app.config.config import settings
from app.config.exceptions import LoginSettinsIsNoneError
from app.config.exceptions import PasswordSettinsIsNoneError



class LoginFlowImpl(LoginFlow):
    def __init__(self, 
        actions:ActionsInt,
        path_to_username:str, 
        path_to_password:str, 
        path_to_login:str,
    ):
        super().__init__(actions)

        if settings.LOGIN is None:
            raise LoginSettinsIsNoneError
        if settings.PASSWORD is None:
            raise PasswordSettinsIsNoneError

        self.modify_to_field:int = 20
        self._enshure_paths_exist([
            path_to_username,
            path_to_password,
            path_to_login
        ])

        self.username:str = settings.LOGIN
        self.password:str = settings.PASSWORD
        self.path_to_username:str = self.base_path + path_to_username
        self.path_to_password:str = self.base_path + path_to_password
        self.path_to_login:str = self.base_path + path_to_login

    def _do_username(self) -> None:
        username_label_x, username_label_y = self.actions.search(self.path_to_username)
        self.actions.left_click(
            username_label_x,
            username_label_y+self.modify_to_field,
        )

        self.actions.write(self.username)

    def _do_password(self) -> None:
        password_label_x,password_label_y = self.actions.search(self.path_to_password)
        # o valor ideal para o mouse descer ate o campo digitavel

        self.actions.left_click(
            password_label_x,
            password_label_y+self.modify_to_field, 
        )
        self.actions.write(self.password)

    def login(self):
        self._do_username()
        self._do_password()

        login_x, login_y = self.actions.search(self.path_to_login)
        self.actions.left_click(
            login_x,
            login_y,
        )

def getLoginFlowImpl(
    actions:ActionsInt,
    path_to_username:str,
    path_to_password:str,
    path_to_login:str,

) -> LoginFlow:
    return LoginFlowImpl(
        actions=actions,
        path_to_username=path_to_username,
        path_to_password=path_to_password,
        path_to_login=path_to_login,
    )