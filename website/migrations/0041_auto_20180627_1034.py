# Generated by Django 2.0.5 on 2018-06-27 07:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0040_auto_20180627_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contesttaskrelationship',
            name='contest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='contest_task_relationship', to='website.Contest'),
        ),
        migrations.AlterField(
            model_name='contesttaskrelationship',
            name='solved',
            field=models.ManyToManyField(blank=True, related_name='contests_tasks_relationship',
                                         to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contesttaskrelationship',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='contest_task_relationship', to='website.Task'),
        ),
    ]