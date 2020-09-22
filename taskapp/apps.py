from django.apps import AppConfig


class TaskappConfig(AppConfig):
    name = 'taskapp'
    def ready(self):
        import taskapp.signals