from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.views import View

class IndexView(View):

    def get(self, request, *args, **kwargs):
        title = 'Главная страница'
        return render(request, 'society_main/index.html', context={
            'title': title,
        })

class AboutView(View):

    def get(self, request, *args, **kwargs):
        title = 'О Нас'
        return render(request, 'society_main/about.html', context={
            'title': title,
        })

class ContactsView(View):

    def get(self, request, *args, **kwargs):
        title = 'Контакты'
        return render(request, 'society_main/contacts.html', context={
            'title': title,
        })

class NewsView(View):

    def get(self, request, *args, **kwargs):
        title = 'Новости'
        return render(request, 'society_main/news.html', context={
            'title': title,
        })