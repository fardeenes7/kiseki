# Generated by Django 4.2.6 on 2023-10-29 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_subcategory_category_specification'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='warranty',
            field=models.IntegerField(default=1),
        ),
    ]
