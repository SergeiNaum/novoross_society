from django.contrib import admin
from django.utils.html import mark_safe

from file_storage.models import FileStorage


@admin.register(FileStorage)
class FileStorageAdmin(admin.ModelAdmin):
    list_display = ('display_photo', 'title', 'image', 'video', 'file')
    list_display_links = ('display_photo', 'title')
    ordering = ['title']
    list_per_page = 10
    search_fields = ['title']
    fields = ['title', 'image', 'video', 'file']
    prepopulated_fields = {'title': ('image', 'video', 'file')}
    save_on_top = True

    @admin.display(description="Изображение")
    def display_photo(self, filestorage: FileStorage):
        if filestorage.image:
            return mark_safe(f"<img src='{filestorage.image.url}' width=50>")
        return "Без фото"

    # def save_imgs(self, request, queryset):
    #
    #     for media in queryset:
    #         # Здесь можно написать логику автоматической обработки и сохранения файлов
    #         pass
    #
    # save_imgs.short_description = "Save photos and videos"
