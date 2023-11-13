from .models import Category

def categories(request):
    categories = Category.objects.all()
    return {'category_context': categories}


def cart(request):
    context = {
        'cart_count': request.user.carts.all().count() if request.user.is_authenticated else 0,
    }
    return context