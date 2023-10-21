# Generated by Django 4.2.6 on 2023-10-21 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('icon', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='ContactFormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('message', models.TextField(verbose_name='Текст обращения')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('photo', models.ImageField(default=None, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('content', models.TextField(blank=True, verbose_name='Текст статьи')),
                ('is_published', models.BooleanField(choices=[(False, 'Черновик'), (True, 'Опубликовано')], default=0, verbose_name='Статус')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='society_main.category', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Статьи',
                'verbose_name_plural': 'Статьи',
                'ordering': ['-time_create'],
                'indexes': [models.Index(fields=['-time_create'], name='society_mai_time_cr_2194ce_idx')],
            },
        ),
    ]