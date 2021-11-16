from django.contrib import admin
from .models import Graphic, Category

# Register your models here.


class GraphicAdmin(admin.ModelAdmin):
    # list display tuple
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'size',
        'orientation',
    )

    # tuple, -sku for reverse order
    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Graphic, GraphicAdmin)
admin.site.register(Category, CategoryAdmin)
