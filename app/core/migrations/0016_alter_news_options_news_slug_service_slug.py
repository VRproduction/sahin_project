# Generated by Django 5.0.2 on 2024-02-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_rename_comleted_project_completed_project_technology'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created'], 'verbose_name': 'Xəbər', 'verbose_name_plural': 'Xəbərlər'},
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
