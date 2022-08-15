from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def alProdCat(request, c_slug=None):
    c_page = None
    products = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.all().filter(category=c_page, available=True)
    else:
        products = Product.objects.all().filter(available=True)
    return render(request, 'category.html', {'category': c_page, 'products': products})
    paginator = Paginator(products, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        p1 = paginator.page(page)
    except (EmptyPage, InvalidPage):
        p1 = paginator.page(paginator.num_pages)


def productdetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})
