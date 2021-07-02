from django.http import HttpResponse
from django.shortcuts import render
from .models import Products

# /products -> index
# uniform Resource Locator (URL Address)
def index(request):
    products = Products.objects.all()
    return render(request, 'index.html',
                  {'products': products})


def new(request):
    return HttpResponse('Welcome to new products')


