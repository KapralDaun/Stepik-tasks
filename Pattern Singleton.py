class Database:
    __instance = None  # ссылка на экземпляр класса

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # если None, то создаем экземляр класса

        return cls.__instance

    def __del__(self):
        Database.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port
