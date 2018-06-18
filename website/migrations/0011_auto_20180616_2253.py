# Generated by Django 2.0.5 on 2018-06-16 19:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0010_auto_20180615_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='tasks', to='website.TaskTag'),
        ),
    ]
