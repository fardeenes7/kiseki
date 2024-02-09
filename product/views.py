from django.shortcuts import render
from .models import *

def index(request):
    context = {
        'categories': Category.objects.all()[:5]
    }
    return render(request, 'index/index.html', context)

def category_list(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'product/category/list.html', context)

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    subcategories = category.subcategories.all()
    context = {
        'category': category,
        'subcategories': subcategories
    }
    return render(request, 'product/category/detail.html', context)



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