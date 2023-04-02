from django.contrib import admin
from .models import MenuItemModel, MenuModel


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent', 'menu_name', 'url',)
    list_filter = ('menu_name',)
    search_fields = ('title', 'slug')
    exclude = ('url',)


admin.site.register(MenuModel, MenuAdmin)
admin.site.register(MenuItemModel, MenuItemAdmin)
