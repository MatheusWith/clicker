class IMGDoesntExistError(Exception):
    def __init__(self, img_name):
        self.message = f"the {img_name} doenst exist"
        super().__init__(self.message)