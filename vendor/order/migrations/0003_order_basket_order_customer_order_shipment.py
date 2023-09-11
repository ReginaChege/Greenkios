# Generated by Django 4.2.3 on 2023-07-08 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_customer_user'),
        ('basket', '0001_initial'),
        ('shippment', '0001_initial'),
        ('order', '0002_order_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='basket',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='basket.basket'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='shipment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shippment.shipment'),
            preserve_default=False,
        ),
    ]
