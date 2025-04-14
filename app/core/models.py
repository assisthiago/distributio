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
    image = models.ImageField(
        "imagem", upload_to="media/items/", blank=True, null=True, default=None
    )
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    # Relationships

    # Functions
    def __str__(self):
        return self.name

    class Meta:
        db_table = "item"
        verbose_name = "item"
        verbose_name_plural = "itens"


class Product(models.Model):

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
        Item,
        verbose_name="adicionais",
        related_name="additional_categories",
        blank=True,
        default=None,
        help_text="Adicionais a este item.",
    )

    # Functions
    def __str__(self):
        return self.title

    class Meta:
        db_table = "additional_category"
        verbose_name = "categoria do adicional"
        verbose_name_plural = "categorias dos adicionais"


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
        verbose_name = "categoria do produto"
        verbose_name_plural = "categorias dos produtos"


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
    delivery_cost = models.DecimalField(
        "custo de entrega",
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
