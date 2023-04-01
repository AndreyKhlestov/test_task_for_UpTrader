from django import template

from ..models import MenuItemModel

register = template.Library()


@register.inclusion_tag('includes/menu.html')
def draw_menu(menu_name):
    menu_items = MenuItemModel.objects.filter(menu_name=menu_name)

    def add_children(menu_item):
        return {
            'item': menu_item,
            'children': [
                add_children(child) for child in menu_item.children.all()
            ]
        }

    menu_tree = [add_children(item) for item in menu_items]
    # from pprint import pprint
    # pprint(menu_tree[0])
    return {'menu_tree': menu_tree}
