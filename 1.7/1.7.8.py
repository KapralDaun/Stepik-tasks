from string import ascii_lowercase, digits


class TextInput:
    MIN_COUNT = 3
    MAX_COUNT = 50
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return "".join(["<p class='login'>", self.name, ": <input type='text' size=", str(self.size), "/>"])

    @classmethod
    def check_name(cls, name):
        Check = True
        if len(name) < 3 or len(name) > 50:
            raise ValueError("некорректное поле name")

        for ch in name:
            if not Check:
                raise ValueError("некорректное поле name")
            for i in cls.CHARS_CORRECT:
                if ch == i:
                    Check = True
                    break


class PasswordInput:
    MIN_COUNT = 3
    MAX_COUNT = 50
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return "".join(["<p class='password'>", self.name, ": <input type='text' size=", str(self.size), "/>"])

    @classmethod
    def check_name(cls, name):
        Check = True
        if len(name) < 3 or len(name) > 50:
            raise ValueError("некорректное поле name")

        for ch in name:
            if not Check:
                raise ValueError("некорректное поле name")
            for i in cls.CHARS_CORRECT:
                if ch == i:
                    Check = True
                    break


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        print(self.login.get_html())
        print(self.password.get_html())
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
