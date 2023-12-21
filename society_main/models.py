from django.db import models
from django.urls import reverse


class TimestampedModel(models.Model):
    """An abstract model with a pair of timestamps."""

    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    class Meta:
        abstract = True


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Post.Status.PUBLISHED)


# Create your models here.
class ContactFormModel(TimestampedModel):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(unique=True, max_length=200, verbose_name='email')
    ip_address = models.GenericIPAddressField(verbose_name='IP отправителя', blank=True, null=True)
    message = models.TextField(verbose_name="Текст обращения")
    checkbox = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def __str__(self):
        return f'Вам письмо от {self.email}'


class Post(TimestampedModel):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    # slug = models.SlugField(max_length=255, db_index=True, blank=True, default='')
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Фото"
    )
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    tags = models.ManyToManyField(
        'TagPost', blank=True, related_name='tags', verbose_name="Теги"
    )
    is_published = models.BooleanField(
        choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
        default=Status.DRAFT, verbose_name="Статус"
    )
    cat = models.ForeignKey(
        'Category', on_delete=models.PROTECT, verbose_name="Категории"
    )
    video = models.FileField(
        upload_to='videos/%Y/%m/%d/', default=None, blank=True, null=True, verbose_name="Видео"
    )
    description = models.TextField(blank=True, verbose_name="Описание к статье")

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    # slug = models.SlugField(max_length=255, db_index=True, blank=True, default='')
    icon = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True, verbose_name="Тэги")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    icon = models.CharField(max_length=100)

    class Meta:
        verbose_name = " Теги"
        verbose_name_plural = "Теги"


    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})
