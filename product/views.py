from django.shortcuts import render
from .models import *

def index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index/index.html', context)

def subcategory_detail(request, slug):
    subcategory = Subcategory.objects.get(slug=slug)
    products = subcategory.products.all()
    context = {
        'subcategory': subcategory,
        'products': products
    }
    return render(request, 'product/subcategory/detail.html', context)


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'product/detail.html', context)


def product_specs(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'product/specs.html', context)


def product_buy(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'product/buy.html', context)

from customer.models import OrderItem
def verify(request,):
    context = {
    }
    sn = request.GET.get('sn')
    if sn:
        try:
            context['product'] = Stock.objects.get(sn=sn).product
            context['stock'] = OrderItem.objects.get(stock__sn=sn)
        except:
            context['error'] = 'Invalid Serial Number'
    return render(request, 'product/verify/verify.html', context)