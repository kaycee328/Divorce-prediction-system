from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dpsproject.apps.users'
    
    def ready(self):
        import dpsproject.apps.users.signals

