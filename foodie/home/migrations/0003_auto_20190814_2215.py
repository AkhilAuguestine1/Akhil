# Generated by Django 2.2.4 on 2019-08-14 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190814_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 14, 22, 15, 47, 215032), verbose_name='date created'),
        ),
    ]