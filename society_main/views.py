from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, FormView


from society_main.forms import ContactForm
from society_main.models import Post, Category, TagPost


class IndexView(View):

    def get(self, request, *args, **kwargs):
        title = 'Главная страница'
        return render(request, 'society_main/index.html', context={
            'title': title, 'active_page': 'index',
        })


class AboutView(View):

    def get(self, request, *args, **kwargs):
        title = 'О Нас'
        return render(request, 'society_main/about.html', context={
            'title': title, 'active_page': 'about',
        })


# class ContactsView(View):
#
#     def get(self, request, *args, **kwargs):
#         title = 'Контакты'
#
#         return render(request, 'society_main/contacts.html', context={
#             'title': title, 'active_page': 'contacts',
#         })
#
#     def post(self, request, *args, **kwargs):
#         title = 'Контакты'
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data.get('name')
#             email = form.cleaned_data.get('email')
#             message = form.cleaned_data.get('message')
#             form.save()
#             messages.success(request, 'Форма была успешно отправлена.')
#             indx = reverse('index')
#             return redirect(indx)
#         return render(request, 'society_main/contacts.html', context={
#             'title': title, 'form': form
#         })



class ContactsView(FormView):
    form_class = ContactForm
    template_name = 'society_main/contacts.html'
    success_url = '/'

    def form_valid(self, form):
        # Обработка валидной формы
        form.save()
        return super().form_valid(form)


class NewsView(View):

    def get(self, request, *args, **kwargs):
        posts = Post.published.all()
        data = {
            'title': 'Новости',
            'posts': posts,
            'cat_selected': 0,
            'active_page': 'news'
        }
        return render(request, 'society_main/news.html', context=data)


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Post.Status.PUBLISHED)
    data = {
        'title': f'Тег: {tag.tag}',
        'posts': posts,
        'cat_selected': None,
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

