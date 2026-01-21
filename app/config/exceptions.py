class IMGDoesntExistError(Exception):
    def __init__(self, img_name):
        self.message = f"the {img_name} doenst exist"
        super().__init__(self.message)

class StartDateSettinsIsNoneError(Exception):
    def __init__(self):
        self.message = "Start date doesn't exists in environment variables"
        super().__init__(self.message)


class EndDateSettinsIsNoneError(Exception):
    def __init__(self):
        self.message = "End date doesn't exists in environment variables"
        super().__init__(self.message)


class LoginSettinsIsNoneError(Exception):
    def __init__(self):
        self.message = "Login doesn't exists in environment variables"
        super().__init__(self.message)

class PasswordSettinsIsNoneError(Exception):
    def __init__(self):
        self.message = "Password doesn't exists in environment variables"
        super().__init__(self.message)