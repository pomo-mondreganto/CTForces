# Generated by Django 2.0.5 on 2018-06-18 08:17

import simplemde.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0023_auto_20180618_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=simplemde.fields.SimpleMDEField(verbose_name='Markdown body'),
        ),
    ]
