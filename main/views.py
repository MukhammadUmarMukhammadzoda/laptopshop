from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from .models import *
from django.http import HttpResponse
# Create your views here.


def index(request):
    brand = Brand.objects.all()
    core_i3Products = Product.objects.filter(CPU__startswith = 'i3')
    core_i5Products = Product.objects.filter(CPU__startswith = 'i5')
    core_i7Products = Product.objects.filter(CPU__startswith = 'i7')
    total = 0

    for work in core_i7Products:
        total+=1
    
    for work in core_i5Products:
        total+=1

    for work in core_i3Products:
        total+=1



    context = {
        'brand':brand,
        'i3':core_i3Products,
        'i5':core_i5Products,
        'i7':core_i7Products,
        'total':total

    }

    return render(request,'index.html', context)

def brand(request, name):
    brand = Brand.objects.all()

    brand2 = Brand.objects.get(name = name)
    core_i3Products = Product.objects.filter(Q(CPU__startswith = 'i3') & Q(brand__name = brand2) )
    core_i5Products = Product.objects.filter(Q(CPU__startswith = 'i5')  & Q(brand__name = brand2))
    core_i7Products = Product.objects.filter(Q(CPU__startswith = 'i7')  & Q(brand__name = brand2))
     
    total = 0

    for work in core_i7Products:
        total+=1
    
    for work in core_i5Products:
        total+=1

    for work in core_i3Products:
        total+=1

    





    context = {
        'brand':brand,
        'i3':core_i3Products,
        'i5':core_i5Products,
        'i7':core_i7Products,
        'total':total

    }

    return render(request,'index.html', context)

def review(request,id):
    brand = Brand.objects.all()

    product = Product.objects.get(id=id)

    return render(request,'review.html',{'product':product, 'brand':brand})