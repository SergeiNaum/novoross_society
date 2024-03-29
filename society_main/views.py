from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, TemplateView, DetailView
from django.utils import timezone


from society_main.forms import ContactForm
from society_main.models import Post, TagPost
from society_main.services.email import send_contact_email_message
from society_main.services.utils import get_client_ip


class IndexView(TemplateView):
    template_name = 'society_main/index.html'
    current_date = timezone.now().date()
    show_announcement = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['active_page'] = 'index'
        if self.current_date.month in [12, 1]:  # Показываем анонс только в декабре и январе
            self.show_announcement = True
        context['show_announcement'] = self.show_announcement
        return context


class AboutView(TemplateView):
    template_name = 'society_main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О Нас'
        context['active_page'] = 'about'
        return context


class PolicyView(TemplateView):
    template_name = 'society_main/policy.html'

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

    def form_valid(self, form):
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.ip_address = get_client_ip(self.request)
            subj = (f'Сообщение из формы обратной связи сайта optimist-novorossyisk от: '
                    f'{feedback.name}')
            send_contact_email_message(
                subj, feedback.email, feedback.message, feedback.ip_address
            )
            feedback.save()

        return super().form_valid(form)


class NewsView(ListView):
    template_name = 'society_main/news.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Статьи'
        context['cat_selected'] = 0
        context['active_page'] = 'news'
        return context

    def get_queryset(self):
        return Post.published.all().select_related('cat')


class NewsTagsView(ListView):

    template_name = 'society_main/news.html'
    context_object_name = 'posts'
    paginate_by = 5
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # tag = context['posts'][0].tags
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        context['title'] = 'Тег: ' + tag.tag
        context['active_page'] = 'news'
        context['cat_selected'] = None
        return context

    def get_queryset(self):
        return Post.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')


class NewsCatsView(ListView):
    template_name = 'society_main/news.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        context['title'] = 'Категория - ' + cat.name
        context['cat_selected'] = cat.id
        context['active_page'] = 'news'
        return context

    def get_queryset(self):
        return Post.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')


class ShowPost(DetailView):
    model = Post
    template_name = 'society_main/post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['active_page'] = 'news'
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(
            Post.published, slug=self.kwargs[self.slug_url_kwarg]
        )


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
