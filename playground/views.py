from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from store.models import Product
from store.models import Customer
from store.models import Collection
from store.models import Order
from store.models import OrderItem
from store.models import Cart
from store.models import CartItem

from django.db.models import Q,F,Value, Func, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg, Sum

from django.db.models import OuterRef, Subquery


# Create your views here.
def say_hello(request):
    # could be none
    # product  = Product.objects.filter(pk=0).first()
    # product  = Product.objects.filter(pk=0).exists()
    
    # keyword = value
    # queryset = Product.objects.filter(unit_price__range=(20, 30))
    # queryset = Product.objects.filter(title__icontains = 'coffee')
    # queryset = Product.objects.filter(title__startswith='coffee')
    # queryset = Product.objects.filter(last_update__year = 2021)
    # queryset = Customer.objects.filter(email__icontains = '.com')
    # queryset = Collection.objects.filter(featured_product__isnull= True)
    # queryset = Product.objects.filter(inventory__lt = 10)
    # queryset = Order.objects.filter(customer_id = 1)
    # queryset = OrderItem.objects.filter(product__collection_id = 3)
    # queryset = Product.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__lt=20))
    
    # Using F object to reference, product__inventory == collection__id 
    # queryset = Product.objects.filter(inventory = F('collection__id'))

    # Sorting
    # queryset = Product.objects.order_by('unit_price', '-title').reverse(    )
    # queryset = Product.objects.all()[5:10]
    # queryset = Product.objects.values_list('id', 'title', 'collection__title')
    # queryset = OrderItem.objects.values('product_id','product__title').order_by('product__title').distinct()
    # queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    
    # select_related (1 to 1)
    # prefetch_related (many to many)
    # queryset = Product.objects.select_related('collection').all()
    #
    # queryset = Product.objects.prefetch_related(
    #    'promotions').select_related('collection').all()
    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    
    # result = Product.objects.filter(collection__id=1).\
    #            aggregate(count = Count('id'), min_price = Min('unit_price'))

    # result = OrderItem.objects.filter(product_id = 1 ).aggregate(sould_count = Sum('quantity'))
    # result = Order.objects.filter(customer_id = 1).aggregate(Count('customer_id'))
    # result = Product.objects.filter(collection_id =3 ).\
     #       aggregate(min_price = Min('unit_price'), max_price = Max('unit_price'), avg_price = Avg('unit_price'))
    #queryset = Customer.objects.annotate(
        # CONCAT
    #    full_name = Func(F('first_name'), Value(' '), 
    #                     F('last_name'), function = 'CONCAT')
    #)

    #queryset = Customer.objects.annotate(
    #    full_name = Concat('first_name', Value(' '),'last_name')
    #)

    # queryset = Customer.objects.annotate(
    #    orders_count = Count('order')
    # )

    #discounted_price = ExpressionWrapper(
    #    F('unit_price') * 0.8, output_field= DecimalField())

    #queryset = Product.objects.annotate(
    #    discounted_price = discounted_price
    #)
    # queryset = Customer.objects.annotate(
    #    last_order_id = Max('order__id')
    # )
    
    # latest = Order.objects.filter(customer=OuterRef('pk')).order_by('-placed_at')

    # queryset = Customer.objects.annotate(
    #     latest_order=Subquery(latest.values('id')[:1]))

    # cartitem5 = CartItem.objects.get(pk=1)
    # cartitem5.quantity = 5
    # cartitem5.save()
    cart = Cart()
    cart.save()

    cartitem1 = CartItem(quantity = 1, cart_id = cart.id, product_id = 1)
    cartitem1.quantity = 2
    cartitem1.save()



    return render(request, 'hello.html', {'name':'Momo'})



    
    # return render(request, 'hello.html', {'name': 'Momo', 'customers': list(queryset)})
    # return render(request, 'hello.html', {'name': 'Momo', 'collections': list(queryset)})
    # return render(request, 'hello.html', {'name':'Momo', 'result': list(queryset)})
    # return render(request, 'hello.html',{'name': 'Momo', 'orders': list(queryset)})