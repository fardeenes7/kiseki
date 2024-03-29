# Generated by Django 4.2.6 on 2024-03-05 19:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_alter_subcategory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='sn',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_hexadecimal', message='Enter a valid hexadecimal number.', regex='^[0-9a-fA-F]*$')]),
        ),
    ]
