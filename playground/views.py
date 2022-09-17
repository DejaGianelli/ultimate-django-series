import re
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, OrderItem


def say_hello(request):
   
   # Be careful with this methods, it can trigger a lot of queries
   # queryset = Product.objects.only('id', 'title')
   queryset = Product.objects.defer('description')
      
   return render(request, 'hello.html', {
      'name': 'Mosh', 
      'products': list(queryset)
   })
