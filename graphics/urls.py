from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_graphics, name='graphics'),
    path('<graphic_id>', views.graphic_detail, name='graphic_detail'),
]
