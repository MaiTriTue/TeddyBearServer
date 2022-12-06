from django.contrib import admin
from django.utils.html import mark_safe
from .models import *


# class ProductsTagInline(admin.TabularInline):
#     model = Products.tags.through


class UserAdmin(admin.ModelAdmin):

    list_display = ['id', 'first_name', 'last_name',
                    'email', 'username', 'password', 'avatar', 'birthday', 'phome', 'address']
    search_fields = ['id', 'first_name', 'last_name',
                     'email', 'username', 'password', 'avatar', 'birthday', 'phome', 'address']
    list_filter = ['username']
    # inlines = (ProductsTagInline,)
    readonly_fields = ['avatar']

    def avatar(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" alt={alt} width="120" />'
                .format(url=obj.image.name, alt=obj.name)
            )


admin.site.register(User, UserAdmin)
