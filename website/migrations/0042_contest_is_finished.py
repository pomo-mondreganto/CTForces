# Generated by Django 2.0.5 on 2018-06-27 07:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0041_auto_20180627_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
    ]
