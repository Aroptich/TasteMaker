from django.contrib import admin
from django.urls import path

from autors.views import AutorCreatView

urlpatterns = [
    path('creat_autor', AutorCreatView.as_view()),
]