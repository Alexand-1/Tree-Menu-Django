from django import template
from ..models import MenuItem

register = template.Library()

@register.inclusion_tag('MenuLinks/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_path = context['request'].path
    menu_items = MenuItem.objects.filter(menu_name=menu_name, is_active=True, parent=None)
    return {'menu': menu_items, 'current_path': current_path}

@register.filter
def has_children(item):
    return item.children.filter(is_active=True).exists()