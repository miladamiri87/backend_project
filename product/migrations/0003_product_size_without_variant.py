# Generated by Django 4.2.9 on 2024-03-29 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_image_product_image_hover_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size_without_variant',
            field=models.TextField(blank=True, null=True),
        ),
    ]
