# Generated by Django 4.2.9 on 2024-03-31 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_color_image_variant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dimension', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='variant',
            name='dimension',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dimension_vars', to='product.color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('none', 'None'), ('color', 'Color'), ('size', 'Size')], default='none', max_length=6),
        ),
    ]