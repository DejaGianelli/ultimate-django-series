import re
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from store.models import Collection, Product, OrderItem, Order, Customer
from tags.models import TaggedItem

# @transaction.atomic
# def say_hello(request):
   
#    order = Order()
#    order.customer_id = 1
#    order.save()
   
#    item = OrderItem()
#    item.order = order
#    item.product_id = 1
#    item.quantity = 1
#    item.unit_price = 10
#    item.save()
   
#    return render(request, 'hello.html', {
#       'name': 'Mosh'
#    })

def say_hello(request):
   
   # ...
   
   with transaction.atomic():
      order = Order()
      order.customer_id = 1
      order.save()
      
      item = OrderItem()
      item.order = order
      item.product_id = -1
      item.quantity = 1
      item.unit_price = 10
      item.save()
   
   return render(request, 'hello.html', {
      'name': 'Mosh'
   })
