# Generated by Django 4.2.9 on 2024-04-27 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0054_category_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='product',
        ),
    ]