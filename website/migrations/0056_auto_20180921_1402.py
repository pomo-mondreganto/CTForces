# Generated by Django 2.1.1 on 2018-09-21 11:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0055_auto_20180705_2116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contest',
            options={'permissions': (('view_unstarted_contest', 'Can view not started contest'),
                                     ('view_running_contest', 'Can view running contest'),
                                     ('can_participate_in_contest', 'Can participate in contest'))},
        ),
    ]
