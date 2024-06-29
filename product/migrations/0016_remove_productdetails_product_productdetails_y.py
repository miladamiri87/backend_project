# Generated by Django 4.2.9 on 2024-03-30 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_rename_product_moreimageofproduct_x'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdetails',
            name='product',
        ),
        migrations.AddField(
            model_name='productdetails',
            name='y',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products_details_info', to='product.product'),
        ),
    ]
