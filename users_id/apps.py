from django.apps import AppConfig
import users_id.routing


class UsersIdConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users_id'
