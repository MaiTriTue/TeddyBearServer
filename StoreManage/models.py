from django.db import models

from CustomUser.models import User
from TeddyBear.models import *

# Create your models here.


class Order(models.Model):
    class Meta:
        ordering = ['id']

    customer_name = models.CharField(max_length=100, null=True)
    customer_address = models.CharField(
        max_length=255, null=False, blank=False)
    customer_email = models.EmailField(max_length=100, null=True)
    note = models.CharField(max_length=255, null=True, blank=True)
    total_amount = models.FloatField(null=True)

    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    customer_user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.customer_name


class CartProduct(models.Model):
    class Meta:
        ordering = ['id', 'create_date_order']

    product_Id = models.CharField(max_length=100, null=False, blank=False)
    amount_product = models.IntegerField(default=1, null=False, blank=False)
    create_date_order = models.CharField(
        max_length=100, null=False, blank=False)
    customer_orderId = models.ForeignKey(
        Order, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.product_Id


class Contact(models.Model):
    admin_name = models.CharField(max_length=100, null=False, default='Admin')
    admin_email = models.EmailField(max_length=100, null=True)
    admin_phone = models.CharField(max_length=20, null=True)
    admin_discription = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.admin_name


class Event(models.Model):
    title = models.CharField(max_length=100, null=False)
    image = models.CharField(max_length=255, null=False)
    discription = models.CharField(max_length=255, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
