# Generated by Django 5.1.7 on 2025-04-14 21:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_additional_delete_item_alter_product_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='título')),
                ('subtitle', models.CharField(max_length=255, verbose_name='subtítulo')),
                ('show', models.BooleanField(default=False, verbose_name='exibir')),
                ('type', models.CharField(choices=[('choose one', 'Escolher um'), ('select multiple', 'Selecionar vários'), ('add on', 'Adicionar mais')], max_length=15, verbose_name='tipo')),
                ('required', models.BooleanField(default=False, verbose_name='obrigatório')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('additionals', models.ManyToManyField(blank=True, default=None, related_name='additional_categories', to='product.additional', verbose_name='adicionais')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='additional_categories', to='product.product', verbose_name='produto')),
            ],
            options={
                'verbose_name': 'Adicional',
                'verbose_name_plural': 'Adicionais',
                'db_table': 'additional_category',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='título')),
                ('subtitle', models.CharField(max_length=255, verbose_name='subtítulo')),
                ('show', models.BooleanField(default=False, verbose_name='exibir')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('products', models.ManyToManyField(blank=True, default=None, help_text='Produtos desta categoria.', related_name='product_categories', to='product.product', verbose_name='produtos')),
            ],
            options={
                'verbose_name': 'produto',
                'verbose_name_plural': 'produtos',
                'db_table': 'product_category',
            },
        ),
    ]
