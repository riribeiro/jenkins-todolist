# Generated by Django 2.1.7 on 2021-09-04 00:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210903_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 3, 21, 40, 3, 663268)),
        ),
    ]
