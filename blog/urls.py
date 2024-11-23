from django.urls import path
from . import views  # from the current directory import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

