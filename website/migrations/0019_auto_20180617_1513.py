# Generated by Django 2.0.5 on 2018-06-17 12:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0018_auto_20180617_1457'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('view_tasks_archive', 'Can view tasks archive'),)},
        ),
    ]
