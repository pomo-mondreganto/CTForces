# Generated by Django 2.0.5 on 2018-06-16 19:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0011_auto_20180616_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='website.TaskTag'),
        ),
    ]