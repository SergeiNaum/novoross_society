# Generated by Django 4.2.6 on 2023-11-03 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('society_main', '0004_contactformmodel_checkbox'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactformmodel',
            options={'ordering': ['-time_create'], 'verbose_name': 'Обратная связь', 'verbose_name_plural': 'Обратная связь'},
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, default=None, null=True, upload_to='videos/%Y/%m/%d/', verbose_name='Видео'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='tagpost',
            name='tag',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Тэги'),
        ),
        migrations.AddIndex(
            model_name='contactformmodel',
            index=models.Index(fields=['-time_create'], name='society_mai_time_cr_e51e1f_idx'),
        ),
    ]
