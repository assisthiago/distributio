from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models


class Client(models.Model):
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
    user = models.OneToOneField(
        User,
        verbose_name="usuário",
        related_name="client",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )

    # Functions
    def __str__(self):
        return self.user.get_full_name()

    def full_name(self):
        return self.__str__()

    full_name.short_description = "nome"

    class Meta:
        db_table = "client"
        verbose_name = "cliente"
        verbose_name_plural = "clientes"


class Address(models.Model):
    # Fields
    zip_code = models.CharField(
        "cep",
        max_length=8,
        validators=[MinLengthValidator(8)],
    )
    street = models.CharField("rua", max_length=255)
    number = models.CharField("número", max_length=10)
    neighborhood = models.CharField("bairro", max_length=255)
    city = models.CharField("cidade", max_length=255)
    state = models.CharField("estado", max_length=2)
    reference = models.CharField(
        "ponto de referência",
        max_length=255,
        blank=True,
        null=True,
        default=None,
    )
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    # Relationships
    user = models.ForeignKey(
        User,
        verbose_name="usuário",
        related_name="addresses",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )

    # Functions
    def __str__(self):
        return self.street

    class Meta:
        db_table = "address"
        verbose_name = "endereço"
        verbose_name_plural = "endereços"
