from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('verify/', verify, name='verify'),

    path('category/all', category_list, name='category_list'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    
    path('subcategory/<slug:slug>/', subcategory_detail, name='subcategory_detail'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('product/<slug:slug>/specs/', product_specs, name='product_specs'),
    path('product/<slug:slug>/buy/', product_buy, name='product_buy'),


]