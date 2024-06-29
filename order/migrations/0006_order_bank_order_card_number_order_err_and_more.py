# Generated by Django 4.2.9 on 2024-04-09 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_coupon_from_date_alter_coupon_to_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='bank',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='card_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='err',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='invoice_id',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='trans_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
