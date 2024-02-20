# Generated by Django 5.0.2 on 2024-02-20 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='services')),
                ('sector', models.CharField(max_length=50)),
                ('scope_of_work', models.BigIntegerField()),
                ('location', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Proyekt',
                'verbose_name_plural': 'Proyektlər',
            },
        ),
        migrations.AlterField(
            model_name='service',
            name='duration',
            field=models.IntegerField(blank=True, null=True, verbose_name='Xidmət müddəti (gün)'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Xidmət haqqı (saat başına)'),
        ),
    ]