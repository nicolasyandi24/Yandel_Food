# Generated by Django 4.1.7 on 2023-05-21 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0009_rename_activo_carrito_compra_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito_compra',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='estado'),
        ),
    ]
