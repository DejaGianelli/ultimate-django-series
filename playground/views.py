import re
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from store.models import Collection, Product, OrderItem, Order, Customer
from tags.models import TaggedItem



def say_hello(request):
   
   collection = Collection()
   collection.title = 'Video Games'
   collection.featured_product = Product(pk=1)
   collection.save()
   print(collection.id)
   
   # Collection.objects.create(name='A', featured_product_id=1)
      
   return render(request, 'hello.html', {
      'name': 'Mosh'
   })
