# Generated by Django 4.2.5 on 2023-12-17 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_coupon_delete_variantimage'),
        ('cart', '0003_order_coupon_applied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='coupon_applied',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.coupon'),
        ),
    ]
