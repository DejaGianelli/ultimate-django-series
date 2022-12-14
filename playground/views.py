import re
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db import connection
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from store.models import Collection, Product, OrderItem, Order, Customer
from tags.models import TaggedItem

def say_hello(request):
   
   return render(request, 'hello.html', {
      'name': 'Mosh'
   })