from django.shortcuts import HttpResponse, render
from store.models import Product


def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {'products': products}
    return render(request, "home.html", context)


def store(request):
    return render(request, "store.html")


def product_detail(request):
    return render(request, "product-detail.html")
