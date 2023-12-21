from django.contrib import admin, messages
from django.utils.html import mark_safe

from .models import Post, Category, ContactFormModel, TagPost


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_photo', 'title', 'time_create', 'is_published', 'cat', 'photo', 'video')
    list_display_links = ('post_photo', 'title')
    list_editable = ('is_published', 'cat')
    ordering = ['-time_create', 'title']
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['title', 'cat__name']
    fields = ['title', 'slug', 'content', 'description', 'cat', 'tags', 'photo', 'video']
    prepopulated_fields = {"slug": ("title",)}
    save_on_top = True

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Post.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записи(ей).")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Post.Status.DRAFT)
        self.message_user(request, f"{count} записи(ей) сняты с публикации!", messages.WARNING)

    @admin.display(description="Изображение")
    def post_photo(self, post: Post):
        if post.photo:
            return mark_safe(f"<img src='{post.photo.url}' width=50>")
        return "Без фото"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


@admin.register(TagPost)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')
    list_display_links = ('id', 'tag')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


@admin.register(ContactFormModel)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Админ-панель модели профил
    """
    list_display = ('name', 'email', 'ip_address', 'message', 'checkbox')
    list_display_links = ('name', 'email', 'ip_address')
    ordering = ['-time_create']
    list_per_page = 10
    search_fields = ['name', 'email']
