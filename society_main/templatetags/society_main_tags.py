from django import template
import society_main.views as views
from society_main.models import Category

register = template.Library()


@register.inclusion_tag('society_main/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}
