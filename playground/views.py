import re
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product


def say_hello(request):
   
   # queryset = Product.objects.order_by('title')
   # queryset = Product.objects.order_by('unit_price', '-title')
   # queryset = Product.objects.order_by('unit_price', '-title').reverse()
   # queryset = Product.objects.filter(collection__id=3).order_by('unit_price')
   # product = Product.objects.order_by('unit_price')[0]
   # product = Product.objects.earliest('unit_price')
   # product = Product.objects.latest('unit_price')
   # queryset = Product.objects.all()[:5]
   queryset = Product.objects.all()[5:10]
   
   return render(request, 'hello.html', {
      'name': 'Mosh', 
      'products': list(queryset)
   })
