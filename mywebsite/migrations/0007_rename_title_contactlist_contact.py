# Generated by Django 3.2 on 2022-01-13 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0006_auto_20220113_1417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactlist',
            old_name='title',
            new_name='contact',
        ),
    ]