from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_graphics, name='graphics'),
    path('<int:graphic_id>/', views.graphic_detail, name='graphic_detail'),
    path('add/', views.add_graphic, name='add_graphic'),
]
