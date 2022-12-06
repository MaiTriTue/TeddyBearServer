from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='userImg/%Y/%m', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    # birthday = models.CharField(max_length=20, blank=True, null=True)
    phome = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100,  blank=True, null=True)

    def __str__(self):
        return self.username


class LikeProducts(models.Model):
    id_product = models.CharField(
        max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.id_product

# Create your models here.


# Create your models here.
