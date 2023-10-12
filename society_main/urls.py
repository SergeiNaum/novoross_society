from django.contrib import admin
from django.urls import path

from society_main.views import IndexView, AboutView, ContactsView, NewsView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('news/', NewsView.as_view(), name='news'),

]