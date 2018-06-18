# Generated by Django 2.0.5 on 2018-06-12 16:50

from django.db import migrations

import website.models_auxiliary


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0006_auto_20180612_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_field',
            field=website.models_auxiliary.CustomFileField(
                upload_to=website.models_auxiliary.CustomUploadTo(append_random=True, path='', upload_type='files')),
        ),
    ]
