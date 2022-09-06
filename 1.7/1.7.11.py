class AppStore:
    list_of_apps = []

    def add_application(self, app):
        self.list_of_apps.append(app)

    def remove_application(self, app):
        self.list_of_apps.remove(app)

    def block_application(self, app):
        app.blocked = True

    def total_apps(self):
        return len(self.list_of_apps)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked

