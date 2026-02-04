from app.flow.flows import LoginFlow
from app.actions.actionsInt import ActionsInt



class LoginFlowImpl(LoginFlow):
    def __init__(self, 
        actions:ActionsInt,
        path_to_username:str, 
        path_to_password:str, 
        path_to_login:str,
        username:str,
        password:str,
        modify_to_field:int,
    ):
        super().__init__(actions)

        self.username:str = username
        self.password:str = password
        self.modify_to_field:int = modify_to_field
        self._enshure_paths_exist([
            path_to_username,
            path_to_password,
            path_to_login
        ])
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

        self.actions.left_click(
            password_label_x,
            password_label_y+self.modify_to_field, 
        )
        self.actions.write(self.password)

    def execute(self):
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
    username:str,
    password:str,
    modify_to_field:int,
) -> LoginFlow:
    return LoginFlowImpl(
        actions=actions,
        path_to_username=path_to_username,
        path_to_password=path_to_password,
        path_to_login=path_to_login,
        username=username,
        password=password,
        modify_to_field=modify_to_field,
    )