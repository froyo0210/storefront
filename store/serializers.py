from decimal import Decimal 
from rest_framework import serializers

from store.models import Product
from store.models import Collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title']

class ProductSerializer(serializers.ModelSerializer):
    # collection = CollectionSerializer()
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory', 'unit_price', 'price_with_tax','collection']
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length = 255)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2, source = 'unit_price')
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset = Collection.objects.all(),
    #     # doesnt have this name to change url
    #     # used to generate hyperlink
    #     view_name='collection-detail'
    # )
    # # # including an object
    # # collection = CollectionSerializer()
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
