# Generated by Django 2.0.5 on 2018-06-17 11:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0016_auto_20180617_1340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': (('view_task', 'Can view task'),)},
        ),
    ]
