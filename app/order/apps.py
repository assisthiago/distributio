from django.apps import AppConfig


class OrderConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app.order"
    verbose_name = "Informações dos pedidos"
