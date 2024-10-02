from collections import defaultdict
from django import template
from tree_menu_app.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']

    menu_items = MenuItem.objects.filter(menu_name=menu_name)
    menu_tree = _build_menu_tree(menu_items)
    active_item = _get_active_item(menu_items, request.path)

    return {
        'menu_items': _build_menu(menu_tree, active_item),
        'active_item': active_item,
        'request': request,
    }


def _get_active_item(menu_items, current_path):
    for item in menu_items:
        if item.get_url() == current_path:
            return item
    return None


def _build_menu_tree(menu_items):
    tree = defaultdict(list)
    for item in menu_items:
        tree[item.parent_id].append(item)
    return tree


def _build_menu(menu_tree, active_item, parent_id=None):
    hierarchy = []
    for item in menu_tree.get(parent_id, []):
        item_data = {
            'item': item,
            'children': _build_menu(menu_tree, active_item, item.id),
            'is_active': item == active_item
        }

        item_data['is_open'] = item_data['is_active'] or any(
            child['is_open'] for child in item_data['children'])

        hierarchy.append(item_data)
    return hierarchy
