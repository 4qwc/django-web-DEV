# Generated by Django 3.2 on 2022-01-13 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0008_rename_contactlist_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='newpassword',
            field=models.TextField(blank=True, null=True),
        ),
    ]