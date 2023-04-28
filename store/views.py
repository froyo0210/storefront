from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer

@api_view(['GET','POST'])
def product_list(request):
    # prevent lazy loading lag
    if request.method == 'GET':
        queryset = Product.objects.select_related('collection').all()
        serialier = ProductSerializer(
            queryset, many = True, context = {'request':request})
        return Response(serialier.data)
    if request.method == 'POST':
        serialier = ProductSerializer(data= request.data)
        serialier.is_valid(raise_exception=True)
        serialier.save()
        # print(serialier.validated_data)
        # serialier.validated_data
        return Response('ok')

@api_view()
def product_detail(request, id):
    # try:
    #     product = Product.objects.get(pk=id)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)
    # except Product.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view()
def collection_detail(request, pk):
    return Response('ok')