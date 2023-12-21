from django.db import models


class FileStorage(models.Model):
    title = models.CharField(max_length=100, verbose_name="название файла")
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    image = models.ImageField(
        upload_to="imgs_st/%Y.%m.%d/", default=None, blank=True, null=True, verbose_name="Изображение"
    )
    video = models.FileField(
        upload_to="vid's_st/%Y.%m.%d/", default=None, blank=True, null=True, verbose_name="Видео"
    )

    file = models.FileField(
        upload_to='files_st/%Y.%m.%d/', default=None, blank=True, null=True, verbose_name="Файл"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Хранилище Файлов'
        verbose_name_plural = 'Хранилище Файлов'
