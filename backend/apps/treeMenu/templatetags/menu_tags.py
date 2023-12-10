from django import template
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('render_menu.html', takes_context=True)
def draw_menu(context, menu_name, item_pk=None):

    menu_items = MenuItem.objects.filter(menu__title=menu_name).select_related('menu','parent').values(
        'id',
        'name',
        'url',
        'parent'
    ).order_by('id')
    
    menu_items = list(menu_items)
    context['menu_items'] = menu_items
    context['item_pk'] = item_pk
    context['menu_name'] = menu_name
    context['roots'] = [item.get('id') for item in menu_items if item.get('parent') is None]
    return context

@register.filter(name='get_children')
def get_children(menu_items, item):
    children = []
    for child in menu_items:
        if child.get('parent') == item.get('id'):
            children.append(child)
            menu_items.remove(child)
    return children