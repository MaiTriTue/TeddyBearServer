from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, status, permissions, generics
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *


class PageSize10Pagiration(PageNumberPagination):
    page_size = 10


class PostViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Post.objects.filter(active=True)
    queryset = queryset.order_by('-create_date')
    serializer_class = PostSerializer
    pagination_class = PageSize10Pagiration

# Create your views here.
