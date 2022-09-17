import re
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, OrderItem, Order


def say_hello(request):
   
   # queryset = Product.objects.select_related('collection').all()
   
   # queryset = Product.objects.prefetch_related('promotions').all()
   
   # queryset = Product.objects.prefetch_related('promotions') \
   #    .select_related('collection') \
   #    .all()
   
   queryset = Order.objects \
      .prefetch_related('orderitem_set__product') \
      .select_related('customer') \
      .order_by('-placed_at')[:5]
      
   return render(request, 'hello.html', {
      'name': 'Mosh', 
      'orders': list(queryset)
   })
