# Generated by Django 4.2.9 on 2024-04-01 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_alter_product_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagRelated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products_tag_related', to='product.product')),
            ],
        ),
    ]