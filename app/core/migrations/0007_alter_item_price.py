# Generated by Django 5.1.7 on 2025-04-08 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='preço'),
        ),
    ]
