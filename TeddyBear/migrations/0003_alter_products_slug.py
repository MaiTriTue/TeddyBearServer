# Generated by Django 4.1.2 on 2022-11-02 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeddyBear', '0002_products_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
