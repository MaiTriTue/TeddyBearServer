import json
import ast
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import requests
from rest_framework import viewsets, status, permissions, generics
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework.decorators import action
from rest_framework.response import Response
from requests.exceptions import HTTPError
# from bs4 import BeautifulSoup


from .models import *
from .serializers import *
from .models import *
from django.conf import settings

# dang ky - dang nhap


def printf(value):
    print('value: ', value)


class UserViewSet(viewsets.ViewSet,
                  generics.ListAPIView,
                  generics.CreateAPIView,
                  generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, JSONParser, FormParser, ]

    @action(methods=['get'], detail=False, url_path='current_user')
    def current_user(self, request):
        return Response(self.serializer_class(request.user).data)

    def get_permissions(self):
        if self.action == 'current_user':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def create(self, request):
        data = {}

        serializer = UserSerializer(
            data=(request.data['params']))

        if serializer.is_valid():
            account = serializer.create()

            data['response'] = 'Successfully registered a new user'
            data['user'] = UserSerializer(
                account, context=self.get_serializer_context()).data
        else:
            data = serializer.errors

        return Response(data)


class LoginViewSet(viewsets.ViewSet):

    permission_classes = [permissions.AllowAny]

    parser_classes = [JSONParser, MultiPartParser, FormParser, ]

    def create(self, request):
        client_app = settings.OAUTH2_INFO
        username = request.data['params']['username']
        password = request.data['params']['password']

        url = 'http://' + request.get_host() + '/o/token/'
        data_dict = {
            'grant_type': 'password',
            'username': username,
            'password': password,
            'client_id': client_app['client_id'],
            'client_secret': client_app['client_secret'],
        }

        aa = requests.post(url, data=data_dict)
        data = json.loads(aa.text)
        token = data.get('access_token', '')

        if token:
            user = User.objects.filter(is_active=True, username=username)
            userSri = UserSerializer(user, many=True)
            like = LikeProducts.objects.filter(user=userSri.data[0]['id'])
            likeSri = LikeProductSerializer(like, many=True)

            return Response(data={
                'infoUser': userSri.data[0],
                'infoLike': likeSri.data,
                'infoAuth': data,
            }, status=status.HTTP_200_OK)
        else:
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


# class LikeUpdateViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView, generics.RetrieveAPIView, generics.DestroyAPIView):
class LikeUpdateViewSet(viewsets.ViewSet):

    parser_classes = [MultiPartParser, JSONParser, FormParser, ]
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        try:
            qry_set = LikeProducts.objects.create(
                id_product=request.data, user=request.user)
            serializer = LikeProductSerializer(qry_set)
        except:
            return Response('Error like product', status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):

        try:
            qry_set = LikeProducts.objects.get(
                id_product=pk, user=request.user)
            qry_set.delete()
        except:
            return Response('Error like product', status=status.HTTP_400_BAD_REQUEST)

        return Response('Delete ------ ok', status=status.HTTP_200_OK)
        # Create your views here.
