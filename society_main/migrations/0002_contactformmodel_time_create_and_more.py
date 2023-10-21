# Generated by Django 4.2.6 on 2023-10-19 18:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('society_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactformmodel',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactformmodel',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Время изменения'),
        ),
        migrations.AlterField(
            model_name='contactformmodel',
            name='message',
            field=models.TextField(verbose_name='Текст обращения'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(blank=True, default='', max_length=255)),
                ('photo', models.ImageField(default=None, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('content', models.TextField(blank=True, verbose_name='Текст статьи')),
                ('is_published', models.BooleanField(choices=[(False, 'Черновик'), (True, 'Опубликовано')], default=0, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статьи',
                'verbose_name_plural': 'Статьи',
                'ordering': ['-time_create'],
                'indexes': [models.Index(fields=['-time_create'], name='society_mai_time_cr_2194ce_idx')],
            },
        ),
    ]
