# Generated by Django 2.2.4 on 2019-08-16 04:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20190815_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 16, 10, 12, 49, 186689), verbose_name='date created'),
        ),
    ]
