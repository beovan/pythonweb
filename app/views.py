from django.shortcuts import render
from django.http import HttpResponse
from.models import *

def home(request):
    products = Product.objects.all()
    context = {'products': products} 
    return render(request, 'home.html',context)
def cart(request):
    if request.user.is_authenticated:
        custormer = request.user.custormer
        order, created = Order.objects.get_or_create(custormer=custormer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
    context = {'items': items, 'order': order}
    return render(request, 'cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        custormer = request.user.custormer
        order, created = Order.objects.get_or_create(custormer=custormer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)