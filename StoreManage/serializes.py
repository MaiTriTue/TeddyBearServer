from rest_framework.serializers import ModelSerializer
from .models import *


class OrderSerialize(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'customer_address', 'customer_email', 'note',
                  'total_amount', 'create_date', 'updated_date', 'status', 'active', 'customer_user', ]


class CartProductSerialize(ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ['id', 'product_Id', 'amount_product',
                  'create_date_order', 'customer_orderId', ]


class ContactSerialize(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'admin_name', 'admin_email',
                  'admin_phone', 'admin_discription', ]


class EventSerialize(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'image', 'discription',
                  'create_date', 'updated_date', 'active', ]
