from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models


class User(AbstractUser):

    # Fields
    cpf = models.CharField(
        "cpf",
        max_length=11,
        unique=True,
        validators=[MinLengthValidator(11)],
        blank=True,
        null=True,
        default=None,
    )
    phone = models.CharField(
        "telefone",
        max_length=11,
        unique=True,
        validators=[MinLengthValidator(11)],
        blank=True,
        null=True,
        default=None,
    )
    birth_date = models.DateField(
        "data de nascimento",
        blank=True,
        null=True,
        default=None,
    )
    created_at = models.DateTimeField(
        "criado em",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        "atualizado em",
        auto_now=True,
    )

    # Relationships

    # Settings
    USERNAME_FIELD = "username"

    # Functions
    def __str__(self):
        return self.get_full_name()

    def full_name(self):
        return self.__str__()

    full_name.short_description = "nome"

    class Meta:
        db_table = "core_user"
        verbose_name = "usuário"
        verbose_name_plural = "usuários"


class Item(models.Model):

    UNIT_CHOICES = (
        ("un", "Unidade"),
        ("g", "Grama"),
        ("kg", "Quilograma"),
        ("ml", "Mililitro"),
        ("l", "Litro"),
    )

    # Fields
    name = models.CharField("nome", max_length=255)
    description = models.TextField("descrição", blank=True, null=True)
    price = models.DecimalField("preço", max_digits=10, decimal_places=2, default=0)
    size = models.IntegerField("tamanho", default=0)
    unit = models.CharField("unidade de medida", max_length=2, choices=UNIT_CHOICES)
    image = models.ImageField("imagem", upload_to="media/items/")
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    # Relationships

    # Functions
    def __str__(self):
        return self.name
