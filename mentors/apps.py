from django.apps import AppConfig


class MentorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mentors'

    def ready(self):
        import mentors.signals  