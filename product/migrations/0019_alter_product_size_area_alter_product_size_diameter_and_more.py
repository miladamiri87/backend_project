# Generated by Django 4.2.9 on 2024-03-31 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size_area',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_diameter',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_height',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_length',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_surface_density',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_thickness',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_weight',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_width',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
    ]
