from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'named_url', 'menu_name', 'is_active')
    list_filter = ('menu_name', 'is_active')
    search_fields = ('name', 'url', 'named_url', 'menu_name')
    list_editable = ('is_active',)

admin.site.register(MenuItem, MenuItemAdmin)

