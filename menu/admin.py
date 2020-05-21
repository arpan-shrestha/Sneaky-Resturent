from django.contrib import admin
from .models import Menu
# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name','description']


admin.site.register(Menu, MenuAdmin)