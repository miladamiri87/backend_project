# Generated by Django 4.2.9 on 2024-03-29 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_moreimageofproduct_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='extra_image',
        ),
    ]