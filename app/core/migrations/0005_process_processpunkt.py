# Generated by Django 5.0.2 on 2024-02-20 13:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_whychooseus_whychooseuspunkt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Biz necə çalışırıq',
                'verbose_name_plural': 'Biz necə çalışırıq',
            },
        ),
        migrations.CreateModel(
            name='ProcessPunkt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='punkts', to='core.process')),
            ],
            options={
                'verbose_name': 'Punkt',
                'verbose_name_plural': 'Punktlar',
            },
        ),
    ]