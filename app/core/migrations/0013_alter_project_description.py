# Generated by Django 5.0.2 on 2024-02-21 12:15

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_hero_slogan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]