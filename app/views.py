from django.shortcuts import render
from django.http import HttpResponse
from.models import *

def home(request):
    products = Product.objects.all()
    context = {'products': products} 
    return render(request, 'home.html',context)
def cart(request): 
    context={}
    return render(request, 'cart.html',context)
def checkout(request): 
    context={}
    return render(request, 'checkout.html', context)