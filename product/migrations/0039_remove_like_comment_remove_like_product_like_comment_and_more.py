# Generated by Django 4.2.9 on 2024-04-03 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0038_like_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='like',
            name='product',
        ),
        migrations.AddField(
            model_name='like',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liked_comments', to='product.comment'),
        ),
        migrations.AddField(
            model_name='like',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liked_products', to='product.product'),
        ),
    ]
