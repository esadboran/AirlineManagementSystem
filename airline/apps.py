from django.apps import AppConfig


class AirlineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'airline'

    def ready(self):
        import airline.signals