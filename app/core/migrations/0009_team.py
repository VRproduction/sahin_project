# Generated by Django 5.0.2 on 2024-02-20 14:08

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_title1_gallery_title_remove_gallery_title2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'verbose_name': 'Üzv',
                'verbose_name_plural': 'Komanda',
            },
        ),
    ]
