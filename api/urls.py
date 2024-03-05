#urls.py

from django.urls import path
from .views import *
from .divisions import get_divisions, get_districts, get_areas

urlpatterns = [
    path('divisions/', get_divisions, name='division_list'),
    path('districts/', get_districts, name='district_list'),
    path('areas/', get_areas, name='area_list'),
]    