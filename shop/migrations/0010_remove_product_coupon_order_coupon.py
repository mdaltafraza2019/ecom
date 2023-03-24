# Generated by Django 4.1.5 on 2023-03-06 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_product_coupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='coupon',
        ),
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.coupon'),
        ),
    ]
