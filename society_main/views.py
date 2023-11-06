from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, FormView, TemplateView, DetailView

from society_main.forms import ContactForm
from society_main.models import Post, TagPost

from society_main.logging import config, file_writer, field
from polog import log

from society_main.services.email import send_contact_email_message
from society_main.services.utils import get_client_ip


class IndexView(TemplateView):
    template_name = 'society_main/index.html'

    @log
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['active_page'] = 'index'
        return context


class AboutView(TemplateView):
    template_name = 'society_main/about.html'

    @log
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О Нас'
        context['active_page'] = 'about'
        return context


class PolicyView(TemplateView):
    template_name = 'society_main/policy.html'

    @log
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Политика обработки персональных данных'
        return context


class ContactsView(FormView):

    form_class = ContactForm
    template_name = 'society_main/contacts.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'title': 'Контакты',
        'active_page': 'contacts'
    }

    # @log
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    def form_valid(self, form):
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.ip_address = get_client_ip(self.request)
            subj = feedback.name
            send_contact_email_message(subj, feedback.email, feedback.message, feedback.ip_address)
            feedback.save()

        return super().form_valid(form)


class NewsView(ListView):
    template_name = 'society_main/news.html'
    context_object_name = 'posts'
    paginate_by = 5

    @log
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Статьи'
        context['cat_selected'] = 0
        context['active_page'] = 'news'
        return context

    @log
    def get_queryset(self):
        return Post.published.all().select_related('cat')


class NewsTagsView(ListView):

    template_name = 'society_main/news.html'
    context_object_name = 'posts'
    paginate_by = 5
    allow_empty = False

    @log
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # tag = context['posts'][0].tags
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        context['title'] = 'Тег: ' + tag.tag
        context['active_page'] = 'news'
        context['cat_selected'] = None
        return context

    @log
    def get_queryset(self):
        return Post.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')


class NewsCatsView(ListView):
    template_name = 'society_main/news.html'
    context_object_name = 'posts'
    paginate_by = 5

    @log
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        context['title'] = 'Категория - ' + cat.name
        context['cat_selected'] = cat.id
        context['active_page'] = 'news'
        return context

    @log
    def get_queryset(self):
        return Post.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')


class ShowPost(DetailView):
    model = Post
    template_name = 'society_main/post.html'
    context_object_name = 'post'

    @log
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['active_page'] = 'news'
        return context

    @log
    def get_object(self, queryset=None):
        return get_object_or_404(Post.published, slug=self.kwargs[self.slug_url_kwarg])


@log
def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

