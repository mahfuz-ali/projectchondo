from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from .views import *


urlpatterns = [

    path('',home, name='search.html'),
    path('data/',data),
    path('district/',district),
    path('chondokotha/',chondokotha),
    path('<int:id>', district, name='district_id'),
]