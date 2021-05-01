from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('class', views.class_name, name='class_name'),
    path('class/lessons', views.lessons_class, name='lessons-class')
]