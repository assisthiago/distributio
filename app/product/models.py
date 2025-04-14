from django.db import models

UNIT_CHOICES = (
    ("un", "Unidade(s)"),
    ("g", "Grama(s)"),
    ("kg", "Quilograma(s)"),
    ("ml", "Mililitro(s)"),
    ("l", "Litro(s)"),
)


class Additional(models.Model):

    # Fields
    name = models.CharField("nome", max_length=255)
    description = models.TextField("descrição", blank=True, null=True)
    price = models.DecimalField(
        "preço",
        max_digits=10,
        decimal_places=2,
        default=0,
        help_text="Máximo de 10 dígitos, 2 casas decimais.",
    )
    size = models.IntegerField(
        "tamanho",
        default=0,
        help_text="Quantidade que vai no item. Ex: 1 un, 180g, 437ml, 1kg...",
    )
    unit = models.CharField("unidade de medida", max_length=2, choices=UNIT_CHOICES)
    image = models.ImageField(
        "imagem", upload_to="media/items/", blank=True, null=True, default=None
    )
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    # Functions
    def __str__(self):
        return self.name

    class Meta:
        db_table = "additional"
        verbose_name = "adicional"
        verbose_name_plural = "adicionais"


class Product(models.Model):

    # Fields
    name = models.CharField("nome", max_length=255)
    description = models.TextField("descrição", blank=True, null=True)
    price = models.DecimalField(
        "preço",
        max_digits=10,
        decimal_places=2,
        default=0,
        help_text="Máximo de 10 dígitos, 2 casas decimais.",
    )
    size = models.IntegerField(
        "tamanho",
        default=0,
        help_text="Quantidade que vai no item. Ex: 1 un, 180g, 437ml, 1kg...",
    )
    unit = models.CharField("unidade de medida", max_length=2, choices=UNIT_CHOICES)
    image = models.ImageField(
        "imagem", upload_to="media/products/", blank=True, null=True, default=None
    )
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    # Functions
    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"
        verbose_name = "produto"
        verbose_name_plural = "produtos"
