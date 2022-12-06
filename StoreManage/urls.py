
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()
router.register('order', views.OrderViewSet, 'order')


urlpatterns = [
    # path('', views.index, name='index'),
    path('', include(router.urls)),
]
