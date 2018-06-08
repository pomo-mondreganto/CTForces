from celery import shared_task
from django.apps import apps
from stdimage.utils import render_variations

get_model = apps.get_model


@shared_task
def process_stdimage(file_name, variations, storage):
    render_variations(file_name, variations, replace=True, storage=storage)
    obj = get_model('website', 'User').objects.get(avatar=file_name)
    obj.avatar_processed = True
    obj.save()


@shared_task
def process_file_upload(checked_files):
    for file in checked_files:
        file.save()
