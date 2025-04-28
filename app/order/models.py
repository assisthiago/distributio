from django.contrib.auth.models import User
from django.db import models

from app.product.models import Product


class Order(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pendente"),
        ("preparing", "Preparando"),
        ("delivering", "Entregando"),
        ("finished", "Finalizado"),
        ("canceled", "Cancelado"),
    )

    PAYMENT_METHOD_CHOICES = (
        ("credit", "Cartão de crédito"),
        ("debit", "Cartão de débito"),
        ("pix", "Pix"),
        ("cash", "Dinheiro"),
    )

    # Fields
    number = models.IntegerField(
        "número do pedido",
        unique=True,
    )
    status = models.CharField(
        "status",
        max_length=25,
        choices=STATUS_CHOICES,
        default="pending",
    )
    payment_method = models.CharField(
        "método de pagamento",
        choices=PAYMENT_METHOD_CHOICES,
        max_length=10,
    )
    delivery = models.BooleanField("entrega", default=False)
    delivery_fee = models.DecimalField(
        "taxa de entrega",
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    delivery_forecast = models.DateTimeField(
        "previsão de entrega",
        blank=True,
        null=True,
        default=None,
    )
    total = models.DecimalField(
        "total",
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    # Relationships
    user = models.ForeignKey(
        User,
        verbose_name="usuário",
        related_name="orders",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )

    products = models.ManyToManyField(
        Product,
        verbose_name="produtos",
        related_name="orders",
        blank=True,
        default=None,
    )

    # Functions
    def __str__(self):
        return f"Pedido #{self.number:03d}"

    class Meta:
        db_table = "order"
        verbose_name = "pedido"
        verbose_name_plural = "pedidos"
