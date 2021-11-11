from django.contrib import admin
from django.urls import path
from . import views

# urls are called by name
urlpatterns = [
    path('', views.all_testimonials, name='all_testimonials'),
    path('add_testimonial', views.add_testimonial, name='add_testimonial'),
    path('edit_testimonial/<item_id>', views.edit_testimonial, name='edit_testimonial'),
    path('delete_testimonial/<item_id>', views.delete_testimonial, name='delete_testimonial'),
]