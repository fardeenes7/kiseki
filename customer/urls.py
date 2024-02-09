from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='user_index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),

    path('cart/', cart, name='cart'),
    path('card/<int:id>/remove', remove_from_cart, name='remove_from_cart'),
    path('cart/<int:id>/add', add_to_cart, name='add_to_cart'),
    path('cart/<int:id>/minus', minus_from_cart, name='minus_from_cart'),
    path('cart/<int:id>/update', update_cart, name='update_cart'),
    
    path('checkout/', checkout, name='checkout'),
    path('orders', order_list, name='order_list'),
    path('orders/<int:id>/', order_detail, name='order_detail'),
    path('orders/<int:id>/cancel', order_cancel, name='order_cancel'),
    path('warranty/', warranty_list, name='warranty_list'),
    path('warranty/<int:id>/', warranty_detail, name='warranty_detail'),    


]