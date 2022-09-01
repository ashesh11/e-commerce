from decimal import Decimal
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from store.models import Collection, OrderItem, Product, Order
from tags.models import TaggedItem

def say_hello(request):
    queryset = Product.objects.raw('SELECT id, title FROM store_product')

    return render(request, 'playground/hello.html', {'name': 'Ashesh', 'result':list(queryset)})
