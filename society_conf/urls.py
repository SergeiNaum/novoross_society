"""
URL configuration for society_conf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.views.decorators.cache import cache_page

from society_conf import settings
from society_main.sitemaps import PostSitemap, CategorySitemap
from society_main.views import page_not_found


sitemaps = {
    'posts': PostSitemap,
    'cats': CategorySitemap,
}

urlpatterns = [
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('', include('society_main.urls')),
    path('captcha/', include('captcha.urls')),
    path('sitemap.xml', cache_page(866000)(sitemap), {'sitemaps': sitemaps},
         name="django.contrib.sitemaps.views.sitemap"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    # urlpatterns = [
    #     path('__debug__/', include(debug_toolbar.urls)),
    # ] + urlpatterns


handler404 = page_not_found
admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Статьи"

