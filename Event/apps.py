from django.apps import AppConfig
from django.db import connection

class EventConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'event'
    def ready(self):
        import event.signals