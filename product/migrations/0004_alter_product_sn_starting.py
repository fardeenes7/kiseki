# Generated by Django 4.2.6 on 2023-10-29 02:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_stock_product_new_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sn_starting',
            field=models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(code='invalid_hexadecimal', message='Enter a valid hexadecimal number.', regex='^[0-9a-fA-F]*$')]),
        ),
    ]
