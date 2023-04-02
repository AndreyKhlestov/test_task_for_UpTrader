from django.shortcuts import render, get_object_or_404
from menu.models import MenuItemModel


def universal_page_test_pages(request):
    # Чтобы не писать для каждого меню title, для тестов беру названия из меню
    slug = request.path.split('/')[-2]
    if slug:
        menu_items = get_object_or_404(MenuItemModel, slug=slug)
        title = menu_items.title
    else:
        title = 'Главное меню'
    ###########################################################################

    context = {'title': title}
    return render(request, 'index.html', context)
