from django.contrib import admin

from .models import MenuItems, MenuCategory
admin.site.register(MenuItems)
admin.site.register(MenuCategory)
