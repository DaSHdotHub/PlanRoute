from django.apps import AppConfig


class RoutingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'routing'
    
    def ready(self):
        import routing.utils
        print('Signals imported')
