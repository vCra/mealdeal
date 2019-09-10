from django.contrib import admin

# Register your models here.
from .models import Item, Category

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category']
    list_editable = ['category']

admin.site.register(Item, ItemAdmin)
admin.site.register(Category)

