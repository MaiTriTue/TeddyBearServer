# Generated by Django 4.1.2 on 2022-11-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreManage', '0003_rename_customer_order_cartproduct_customer_orderid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='create_date_order',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]