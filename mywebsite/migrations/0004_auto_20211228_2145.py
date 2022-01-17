# Generated by Django 3.2 on 2021-12-28 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0003_rename_cost_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='instock',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]