from django.apps import AppConfig


class managementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.management'

    def ready(self):
        import apps.management.signals
