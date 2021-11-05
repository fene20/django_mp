from django.urls import path
# import from current directory
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag')
]
