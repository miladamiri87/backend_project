# Generated by Django 4.2.9 on 2024-03-29 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_size_without_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size_without_variant',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]