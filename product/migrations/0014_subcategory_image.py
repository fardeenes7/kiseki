# Generated by Django 4.2.6 on 2024-02-09 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_rename_image_subcategory_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='subcategory/'),
        ),
    ]
