# Generated by Django 2.0.5 on 2018-06-15 19:27

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0009_auto_20180612_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contest',
            old_name='datetime',
            new_name='start_time',
        ),
        migrations.AddField(
            model_name='contest',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2035, 1, 1, 3, 1, 40)),
        ),
    ]
