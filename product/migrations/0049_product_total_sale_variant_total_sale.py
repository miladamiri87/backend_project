# Generated by Django 4.2.9 on 2024-04-21 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0048_pricechange'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total_sale',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='variant',
            name='total_sale',
            field=models.PositiveIntegerField(default=0),
        ),
    ]