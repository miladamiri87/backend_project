# Generated by Django 4.2.9 on 2024-03-31 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_alter_product_size_area_alter_product_size_diameter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='image_variant',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d/'),
        ),
    ]
