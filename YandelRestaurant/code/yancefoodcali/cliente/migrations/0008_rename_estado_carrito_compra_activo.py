# Generated by Django 4.1.7 on 2023-05-21 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0007_alter_carrito_compra_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrito_compra',
            old_name='estado',
            new_name='activo',
        ),
    ]
