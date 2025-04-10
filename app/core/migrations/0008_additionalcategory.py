# Generated by Django 5.1.7 on 2025-04-08 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_item_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='nome')),
                ('subtitle', models.CharField(max_length=255, verbose_name='nome')),
                ('show', models.BooleanField(default=False, verbose_name='exibir')),
                ('type', models.CharField(choices=[('choose one', 'Escolher'), ('add on', 'Adicionar')], max_length=10, verbose_name='tipo')),
                ('required', models.BooleanField(default=False, verbose_name='obrigatório')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('additionals', models.ManyToManyField(blank=True, default=None, help_text='Adicionais a este item.', null=True, related_name='additionals', to='core.item', verbose_name='adicionais')),
            ],
        ),
    ]
