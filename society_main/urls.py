from django.urls import path
from django.urls import re_path
from django.views.decorators.cache import cache_page


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
    path('', cache_page(30000)(IndexView.as_view()), name='index'),
    path('about/', cache_page(30000)(AboutView.as_view()), name='about'),
    path('contacts/', cache_page(6)(ContactsView.as_view()), name='contacts'),
    path('news/', cache_page(1000)(NewsView.as_view()), name='news'),
    path('news/post/<slug:slug>/', cache_page(30000)(ShowPost.as_view()), name='post'),
    path('category/<slug:cat_slug>/', cache_page(10)(NewsCatsView.as_view()), name='category'),
    path('tags/<slug:tag_slug>/', cache_page(10)(NewsTagsView.as_view()), name='tag'),
    path('policy/', cache_page(30000)(PolicyView.as_view()), name='policy'),
    re_path(
        r'^manifest\.json$', TemplateView.as_view(
            template_name='manifest.json', content_type='application/json')
    ),

]
