from django.db import models
from TeddyBear.models import ItemBase

from ckeditor.fields import RichTextField


class CategoryPost(models.Model):
    class Meta:
        ordering = ['id']
    name = models.CharField(null=False, max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(ItemBase):
    class Meta:
        ordering = ['id']
        unique_together = ('name', 'category')

    content = RichTextField()

    image = models.CharField(max_length=255, null=True, blank=True)
    like = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(
        CategoryPost, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


# Create your models here.
