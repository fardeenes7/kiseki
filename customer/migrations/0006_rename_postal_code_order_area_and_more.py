# Generated by Django 4.2.6 on 2024-03-05 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_orderitem_warranty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='postal_code',
            new_name='area',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='city',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='state',
            new_name='division',
        ),
    ]
