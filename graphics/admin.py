from django.contrib import admin

# Register your models here.


from .models import Graphic, Category

# Register your models here.
admin.site.register(Graphic)
admin.site.register(Category)