# Generated by Django 2.0.5 on 2018-06-02 07:43

from django.db import migrations, models

import website.models_auxiliary


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0003_auto_20180601_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_field',
            field=website.models_auxiliary.CustomFileField(blank=True, null=True,
                                                           upload_to=website.models_auxiliary.CustomUploadTo(
                                                               append_random=True, path='', upload_type='files')),
        ),
    ]
