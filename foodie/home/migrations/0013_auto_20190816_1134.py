# Generated by Django 2.2.4 on 2019-08-16 06:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20190816_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 16, 11, 34, 42, 561199), verbose_name='date created'),
        ),
    ]
