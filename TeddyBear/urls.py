
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()
router.register('products', views.ProductViewSet, 'products')
router.register('new-products', views.NewProductViewSet, 'new-products')
router.register('teddy-bear-hot', views.TeddyBearHotViewSet, 'teddy-bear-hot')
router.register('bouquet-hot', views.BouquetHotViewSet, 'bouquet-hot')
router.register('gift-box-hot', views.GiftBoxHotViewSet, 'gift-box-hot')
router.register('gau-bong', views.GauBongViewSet, 'gau-bong')
router.register('thu-bong', views.ThuBongViewSet, 'thu-bong')
router.register('goi-bong', views.GoiBongViewSet, 'goi-bong')
router.register('gau-bong-hoat-hinh',
                views.GauBongHoatHinhViewSet, 'gau-bong-hoat-hinh')
router.register('bup-be', views.BupBeViewSet, 'bup-be')
router.register('hong-sap', views.HongSapViewSet, 'hong-sap')
router.register('hoa-tien', views.HoaTienViewSet, 'hoa-tien')

router.register('nail-hot', views.NailHotViewSet, 'nail-hot')
router.register('nail', views.NailViewSet, 'nail')
router.register('son', views.SonViewSet, 'son')
router.register('socola', views.SocolaViewSet, 'socola')
router.register('my-pham', views.MyPhamViewSet, 'my-pham')
router.register('blog-qua-tang', views.QuaTangViewSet, 'blog-qua-tang')
router.register('blog-lam-dep', views.BeautyfulViewSet, 'blog-lam-dep')
router.register('blog-chinh-hang',
                views.CheckGenuineViewSet, 'blog-chinh-hang')
router.register('search-name-list',
                views.SearchNameListViewSet, 'search-name-list')
router.register('best-seller',
                views.ProductBestSellerViewSet, 'best-seller')


urlpatterns = [
    # path('', views.index, name='index'),
    path('', include(router.urls)),
]
