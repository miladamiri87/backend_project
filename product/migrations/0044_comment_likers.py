# Generated by Django 4.2.9 on 2024-04-03 18:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0043_remove_comment_likers_product_likers'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likers',
            field=models.ManyToManyField(blank=True, related_name='comment_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]