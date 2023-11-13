from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('verify/', verify, name='verify'),

    path('subcategory/<slug:slug>/', subcategory_detail, name='subcategory_detail'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('product/<slug:slug>/specs/', product_specs, name='product_specs'),
    path('product/<slug:slug>/buy/', product_buy, name='product_buy'),


]