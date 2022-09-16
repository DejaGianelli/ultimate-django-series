import re
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

def say_hello(request):
   queryset = Product.objects.all()
   
   for product in queryset:
      print(product)
   
   return render(request, 'hello.html', {'name': 'Mosh'})
