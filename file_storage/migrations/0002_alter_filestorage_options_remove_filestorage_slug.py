# Generated by Django 4.2.6 on 2023-12-19 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_storage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filestorage',
            options={'verbose_name': 'Хранилище Файлов', 'verbose_name_plural': 'Хранилище Файлов'},
        ),
        migrations.RemoveField(
            model_name='filestorage',
            name='slug',
        ),
    ]
