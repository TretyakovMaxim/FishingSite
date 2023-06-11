from django import template
from blog.models import *

register = template.Library()


@register.simple_tag()  # В аргументах можно прописать какие либо имя например (name='getcats') и использовать его
# вместо имени функции
def get_categories():
    return Category.objects.all()


@register.inclusion_tag("blog/list_categories.html")
def show_categories():
    categories = Category.objects.all()
    return {"categories": categories}


@register.inclusion_tag("blog/list_menu.html")
def show_menu():
    menu = [{'title': 'О сайте', 'url_name': 'about'},
            {'title': 'Добавить статью', 'url_name': 'add_page'},
            {'title': 'Обратная связь', 'url_name': 'contact'}, ]

    return {'menu': menu}
