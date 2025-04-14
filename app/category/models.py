from django.db import models

from app.product.models import Additional, Product


class AdditionalCategory(models.Model):
    TYPE_CHOICES = (
        ("choose one", "Escolher um"),
        ("select multiple", "Selecionar vários"),
        ("add on", "Adicionar mais"),
    )

    # Fields
    title = models.CharField("título", max_length=255)
    subtitle = models.CharField("subtítulo", max_length=255)
    show = models.BooleanField("exibir", default=False)
    type = models.CharField(
        "tipo",
        max_length=15,
        choices=TYPE_CHOICES,
    )
    required = models.BooleanField("obrigatório", default=False)
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    # Relationships
    product = models.ForeignKey(
        Product,
        verbose_name="produto",
        related_name="additional_categories",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )

    additionals = models.ManyToManyField(
        Additional,
        verbose_name="adicionais",
        related_name="additional_categories",
        blank=True,
        default=None,
    )

    # Functions
    def __str__(self):
        return self.title

    class Meta:
        db_table = "additional_category"
        verbose_name = "Adicional"
        verbose_name_plural = "Adicionais"


class ProductCategory(models.Model):
    # Fields
    title = models.CharField("título", max_length=255)
    subtitle = models.CharField("subtítulo", max_length=255)
    show = models.BooleanField("exibir", default=False)
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    # Relationships
    products = models.ManyToManyField(
        Product,
        verbose_name="produtos",
        related_name="product_categories",
        blank=True,
        default=None,
        help_text="Produtos desta categoria.",
    )

    # Functions
    def __str__(self):
        return self.title

    class Meta:
        db_table = "product_category"
        verbose_name = "produto"
        verbose_name_plural = "produtos"
