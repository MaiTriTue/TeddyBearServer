from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from datetime import datetime
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'email', 'username', 'password', 'avatar', 'birthday', 'phome', 'address']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self):
        user = User(**self.validated_data)
        user.set_password(self.validated_data['password'])

        user.save()
        return user


class LikeProductSerializer(ModelSerializer):
    class Meta:
        model = LikeProducts
        fields = ['id', 'id_product', 'user']
