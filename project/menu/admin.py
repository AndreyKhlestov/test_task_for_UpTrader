from django.contrib import admin
from .models import MenuItemModel


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent', 'menu_name', 'url',)
    list_filter = ('menu_name',)
    search_fields = ('title', 'slug')
    exclude = ('url',)


admin.site.register(MenuItemModel, MenuItemAdmin)
