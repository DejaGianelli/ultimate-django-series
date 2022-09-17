import re
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, OrderItem, Order, Customer


def say_hello(request):
   
   # queryset = Customer.objects.annotate(is_new=Value(True))
   queryset = Customer.objects.annotate(new_id=F('id') + 1)
      
   return render(request, 'hello.html', {
      'name': 'Mosh', 
      'result': list(queryset)
   })
