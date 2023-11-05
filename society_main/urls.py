from django.contrib import admin
from django.urls import path
from django.urls import re_path




from society_main.views import (
    IndexView,
    AboutView,
    ContactsView,
    NewsView,
    ShowPost,
    NewsCatsView,
    NewsTagsView,
    PolicyView,
    TemplateView,
)
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('news/', NewsView.as_view(), name='news'),
    path('news/post/<slug:slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', NewsCatsView.as_view(), name='category'),
    path('tags/<slug:tag_slug>/', NewsTagsView.as_view(), name='tag'),
    path('policy/', PolicyView.as_view(), name='policy'),
    re_path(r'^manifest\.json$', TemplateView.as_view(template_name='manifest.json', content_type='application/json')),

]
