from rest_framework import viewsets
from rest_framework import viewsets, status, permissions, generics
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.response import Response
import json
# from requests.exceptions import HTTPError
from .models import *
from .serializes import *
from CustomUser.models import User
from CustomUser.serializers import *
from TeddyBear.models import Products
from TeddyBear.serializes import ProductSerialize


class PageSize24Pagiration(PageNumberPagination):
    page_size = 24


class OrderViewSet(viewsets.ViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        dataOrder = request.data
        if dataOrder:
            if dataOrder['customer_userId']:
                user = User.objects.get(pk=dataOrder['customer_userId'])
            else:
                user = User.objects.get(pk=2)

            # Create order
            order = Order.objects.create(
                customer_name=dataOrder['customer_name'],
                customer_address=dataOrder['customer_address'],
                customer_email=dataOrder['customer_email'],
                note=dataOrder['note'],
                total_amount=dataOrder['total_amount'],
                customer_user=user,
            )
            orderSeri = OrderSerialize(order, many=False)
            if dataOrder['dataProducts']:
                data = json.loads(dataOrder['dataProducts'])
                for item in data:
                    # Create product in cart
                    CartProduct.objects.create(
                        product_Id=item['id'],
                        amount_product=item['count'],
                        create_date_order=orderSeri['create_date'].value,
                        customer_orderId=order,
                    )

                cartProduct = CartProduct.objects.filter(
                    create_date_order=orderSeri['create_date'].value, customer_orderId=order)
                cartProductSeri = CartProductSerialize(cartProduct, many=True)

                return Response(data={
                    'order': orderSeri.data,
                    'products': cartProductSeri.data,
                }, status=status.HTTP_201_CREATED)

        return Response('field !!!', status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        dataCart = []
        try:
            user = User.objects.get(pk=pk)

            if user:
                order = Order.objects.filter(customer_user=pk)
                orderInfo = OrderSerialize(order, many=True)

                for item in orderInfo.data:
                    cartProduct = CartProduct.objects.filter(
                        create_date_order=orderInfo.data[0]['create_date'], customer_orderId=orderInfo.data[0]['id'])
                    cartProductSeri = CartProductSerialize(
                        cartProduct, many=True)

                    for proItem in cartProductSeri.data:
                        product = Products.objects.filter(
                            pk=proItem['product_Id'])
                        productSeri = ProductSerialize(product, many=True)
                        try:
                            if productSeri.data[0]:
                                pro = productSeri.data[0]
                        except:
                            pro = ''

                        proItem.update({'productInfo': pro})
                        dataCart.append(proItem)

                        print('------- 5: ',
                              proItem['product_Id'], ' --- ', dataCart)

            return Response(data={
                'order': orderInfo.data,
                'products': dataCart,
            }, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # def destroy(self, request, pk):
    #     try:
    #         a = [34, 35, 37, 38, 39]
    #         for item in a:
    #             order = Order.objects.get(customer_user=pk, id=item)
    #             if order:
    #                 order.delete()
    #                 # order.save()
    #                 print('destroy: ', order)

    #         return Response(data='Done !', status=status.HTTP_200_OK)
    #     except:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)


class CartProductViewset(viewsets.ViewSet):
    permissions_class = [permissions.AllowAny]

    def create(self, request):
        cartData = request.data

        return Response(cartData, status=status.HTTP_201_CREATED)
