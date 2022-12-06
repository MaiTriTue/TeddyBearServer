from django.contrib import admin
from django.utils.html import mark_safe
from .models import *


# class ProductsTagInline(admin.TabularInline):
#     model = Products.tags.through


class OrderAdmin(admin.ModelAdmin):

    list_display = ['id', 'customer_name', 'customer_address', 'customer_email', 'note',
                    'total_amount', 'create_date', 'updated_date', 'status', 'active', 'customer_user', ]
    search_fields = ['id', 'customer_name', 'customer_address', 'customer_email', 'note',
                     'total_amount', 'create_date', 'updated_date', 'status', 'active', 'customer_user', ]
    list_filter = ['create_date', 'status', 'customer_name']
    # inlines = (ProductsTagInline,)


class ContactAdmin(admin.ModelAdmin):

    list_display = ['id', 'admin_name', 'admin_email',
                    'admin_phone', 'admin_discription', ]
    search_fields = ['id', 'admin_name', 'admin_email',
                     'admin_phone', 'admin_discription', ]
    list_filter = ['admin_name']

    readonly_fields = ['avatar']

    def avatar(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'
                .format(url=obj.image.name)
            )


class EventAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'image', 'discription',
                    'create_date', 'updated_date', 'active', ]
    search_fields = ['id', 'title', 'image', 'discription',
                     'create_date', 'updated_date', 'active', ]
    list_filter = ['title']

    readonly_fields = ['avatar']

    def avatar(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'
                .format(url=obj.image.name)
            )


admin.site.register(Order, OrderAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Event, EventAdmin)
