from django.contrib import admin
from django.utils.html import mark_safe
from .models import *


admin.site.register(Category)
admin.site.register(ChildrentCategory)
# admin.site.register(Products)


# Register your models here.

# class ProductsTagInline(admin.TabularInline):
#     model = Products.tags.through


class ProductsAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'create_date', 'updated_date', 'active', 'discription', 'amount_sold', 'like',
                    'size', 'color', 'initial_price', 'curent_price', 'discount_product', 'hot_product', 'childrent_category']
    search_fields = ['id', 'name', 'create_date', 'updated_date', 'active', 'discription', 'amount_sold', 'like',
                     'size', 'color', 'initial_price', 'curent_price', 'discount_product', 'hot_product', 'childrent_category']

    list_filter = ['name']
    # inlines = (ProductsTagInline,)
    readonly_fields = ['avatar']

    def avatar(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'
                .format(url=obj.image.name)
            )


admin.site.register(Products, ProductsAdmin)
