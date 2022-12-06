from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from datetime import datetime
from .models import *


class CategoryPostSerializer(ModelSerializer):
    class Meta:
        model = CategoryPost
        fields = ['id', 'name']


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'name',  'image', 'content', 'create_date',
                  'updated_date',  'category']
