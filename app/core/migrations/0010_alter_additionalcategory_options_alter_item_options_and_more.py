# Generated by Django 5.1.7 on 2025-04-08 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_additionalcategory_additionals'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='additionalcategory',
            options={'verbose_name': 'categoria do adicional', 'verbose_name_plural': 'categorias dos adicionais'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'item', 'verbose_name_plural': 'itens'},
        ),
        migrations.AlterModelTable(
            name='additionalcategory',
            table='additional_category',
        ),
        migrations.AlterModelTable(
            name='item',
            table='item',
        ),
    ]
