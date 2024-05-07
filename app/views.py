from django.shortcuts import render
from django.http import HttpResponse

def home(request): 
    return render(request, 'home.html')
def cart(request): 
    context={}
    return render(request, 'cart.html',context)
def checkout(request): 
    context={}
    return render(request, 'checkout.html', context)