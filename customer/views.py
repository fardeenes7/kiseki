from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import *
from product.models import *
from django.contrib import messages
# Create your views here.

def index(request):
    context = {
        'orders': request.user.orders.all().order_by('-id')[:5],
        'warranties': Warranty.objects.filter(sn__in=Stock.objects.filter(product__in=Product.objects.filter(order_items__order__user=request.user))).order_by('-id')[:5]
    }
    return render(request, 'user/index.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('user_index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            return redirect('user_index') 
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'auth/login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('user_index')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        name = request.POST.get('name').split()
        first_name = ' '.join(name[:-1])
        last_name = name[-1]
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            messages.error(request, 'Password does not match')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
        user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
        user.set_password(password)
        user.save()
        auth_login(request, user)
        messages.success(request, 'Account created successfully')
        return redirect('user_index')
    return render(request, 'auth/register.html')

def logout(request):
    auth_logout(request)
    return redirect('index')


def cart(request):
    context = {
        'cart': request.user.carts.all()
    }
    return render(request, 'user/cart.html', context)


def remove_from_cart(request, id):
    cart = request.user.carts.get(id=id)
    cart.delete()
    messages.success(request, 'Product removed from cart')
    return redirect('cart')


def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    cart = request.user.carts.filter(product=product).first()
    if cart and product.stock() > cart.quantity:
        cart.quantity += 1
        cart.save()
    else:
        cart = Cart.objects.create(user=request.user, product=product)
    messages.success(request, 'Product added to cart.')
    return redirect('cart')


def minus_from_cart(request, id):
    cart = request.user.carts.get(id=id)
    if cart.quantity > 1:
        cart.quantity -= 1
        cart.save()
    else:
        cart.delete()
    messages.success(request, 'Product quantity updated.')
    return redirect('cart')


def update_cart(request, id):
    cart = request.user.carts.get(id=id)
    product = cart.product
    quantity = int(request.GET.get('quantity'))
    if product.stock() >= quantity:
        cart.quantity = quantity
        messages.success(request, 'Product quantity updated.')
    else:
        messages.error(request, 'Product quantity exceeded our stock. Max quantity is ' + str(product.stock()))
    cart.save()
    return redirect('cart')


def checkout(request):
    context = {
        'cart': request.user.carts.all()
    }
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            city = request.POST.get('city')
            postal_code = request.POST.get('postal_code')
            state = request.POST.get('state')
            order = Order.objects.create(user=request.user, name=name, phone=phone, address=address, city=city, postal_code=postal_code, state=state)
            for cart in request.user.carts.all():
                for _ in range(cart.quantity):
                    OrderItem.objects.create(order=order, product=cart.product)
            request.user.carts.all().delete()
            messages.success(request, 'Order placed successfully')
            return redirect('order_list')
        except Exception as e:
            print(e)
            messages.error(request, 'Something went wrong')
    return render(request, 'user/checkout.html', context)


def order_list(request):
    context = {
        'orders': request.user.orders.all()
    }
    return render(request, 'user/order/list.html', context)


def order_detail(request, id):
    STATUS_VALUE = {
        'Pending': 1,
        'Processing': 3,
        'Shipped': 5,
        'Delivered': 8,
        'Cancelled': 5
    }
    order = request.user.orders.get(id=id)
    context = {
        'order': order,
        'status_value': STATUS_VALUE[order.status],
    }
    return render(request, 'user/order/detail.html', context)


def order_track(request, id):
    return render(request, 'user/order/track.html')


def order_cancel(request, id):
    order = request.user.orders.get(id=id)
    order.status = 'Cancelled'
    order.save()
    messages.success(request, 'Order cancelled successfully')
    return redirect('order_list')

def warranty_list(request):
    context = {
        'warranties': Warranty.objects.filter(sn__in=Stock.objects.filter(product__in=Product.objects.filter(order_items__order__user=request.user)))
    }
    return render(request, 'user/warranty/list.html', context)


def warranty_detail(request, id):
    warranty = Warranty.objects.get(id=id)
    context = {
        'warranty': warranty,
        'logs': warranty.logs.all().order_by('-id'),
        'product': warranty.sn.product,
        'order_item': OrderItem.objects.get(stock=warranty.sn),
    }

    return render(request, 'user/warranty/detail.html', context)





