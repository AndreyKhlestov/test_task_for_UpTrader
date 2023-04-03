from django import template

from ..models import MenuItemModel


register = template.Library()


@register.inclusion_tag('includes/menu.html')
def draw_menu(menu_name, request):
    def add_children(menu_item):
        children = None
        if menu_item.url in request.path:
            children = [
                add_children(child) for child in menu_item.children.all()
            ]

        return {
            'item': menu_item,
            'children': children
        }

    first_menu_item = MenuItemModel.objects.filter(
        menu_name__name=menu_name,
        parent=None
        )

    menu_tree = [add_children(item) for item in first_menu_item]
    return {'menu_tree': menu_tree, 'request': request}
