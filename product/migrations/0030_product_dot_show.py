# Generated by Django 4.2.9 on 2024-04-01 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0029_product_scroll_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dot_show',
            field=models.BooleanField(default=False),
        ),
    ]