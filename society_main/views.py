from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.contrib import messages
from django.views import View

from society_main.forms import ContactForm
from society_main.models import Post, Category

cats_db = [
    {'id': 1, 'name': 'Досуг+'},
    {'id': 2, 'name': 'Льготы+'},

]


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
            'title': title
        })

    def post(self, request, *args, **kwargs):
        title = 'Контакты'
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            form.save()
            messages.success(request, 'Форма была успешно отправлена.')
            indx = reverse('index')
            return redirect(indx)
        return render(request, 'society_main/contacts.html', context={
            'title': title, 'form': form
        })


class NewsView(View):

    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(is_published=1)
        data = {
            'title': 'Новости',
            'posts': posts,
            'cat_selected': 0,
        }

        return render(request, 'society_main/news.html', context=data)


def show_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    data = {
        'title': post.title,
        'post': post,
        'cat_selected': 1,
    }

    return render(request, 'society_main/post.html', context=data)


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Post.published.filter(cat_id=category.pk)
    data = {
        'title': f'Рубрика: {category.name}',
        'posts': posts,
        'cat_selected': category.pk,
    }

    return render(request, 'society_main/news.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

