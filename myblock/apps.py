from django.apps import AppConfig


class MyblockConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myblock'
    def ready(self):
        import myblock.signals

