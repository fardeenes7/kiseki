# Generated by Django 4.2.6 on 2023-10-29 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='new_stock',
        ),
    ]
