from django.apps import AppConfig


class UserinterfaceConfig(AppConfig):
    name = 'UserInterface'

    def ready(self):
        import UserInterface.signals