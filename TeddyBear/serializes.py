from rest_framework.serializers import ModelSerializer
from .models import *


class ProductSerialize(ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name',  'image', 'discription',  'color',
                  'size', 'material', 'amount_sold', 'initial_price',
                  'curent_price',
                  'amount_sold',
                  'discount_product',
                  'hot_product', 'childrent_category']
