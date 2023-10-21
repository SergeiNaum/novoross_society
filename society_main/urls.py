from django.contrib import admin
from django.urls import path

from society_main.views import IndexView, AboutView, ContactsView, NewsView, show_post, show_category

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('news/', NewsView.as_view(), name='news'),
    path('news/post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:cat_slug>/', show_category, name='category'),

]