# Generated by Django 4.2.9 on 2024-04-08 14:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0003_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('discount', models.PositiveIntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('from_date', models.DateTimeField(auto_now_add=True)),
                ('to_date', models.DateTimeField(auto_now_add=True)),
                ('user_exclude', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
