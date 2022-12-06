from django.contrib import admin
from django import forms
from django.utils.html import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


class CategoryPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    list_filter = ['name']


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = "__all__"


class PostAdmin(admin.ModelAdmin):

    form = PostForm
    list_display = ['id', 'name',  'image', 'content', 'create_date',
                    'updated_date',  'category']
    search_fields = ['id', 'name',  'image', 'content', 'create_date',
                     'updated_date',  'category']
    list_filter = ['name']
    # inlines = (ProductsTagInline,)
    readonly_fields = ['avatar']

    def avatar(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" alt={alt} width="120" />'
                .format(url=obj.image.name, alt=obj.name)
            )


admin.site.register(Post, PostAdmin)
admin.site.register(CategoryPost, CategoryPostAdmin)

# Register your models here.
