from rest_framework import viewsets
from rest_framework import viewsets, status, permissions, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializes import *

CategoryData = ['Gau', 'Hoa', 'Hop qua', 'BeautyProduct', 'Blog']
childrentCategoryData = [
    {
        'category': 'Gau',
        'childrent': 'Gau bong',
    },
    {
        'category': 'Gau',
        'childrent': 'Thu bong',
    },
    {
        'category': 'Gau',
        'childrent': 'Hoat hinh',
    },
    {
        'category': 'Gau',
        'childrent': 'Goi bong',
    },
    {
        'category': 'Gau',
        'childrent': 'Bup be',
    },
    {
        'category': 'Hoa',
        'childrent': 'Hong sap',
    },
    {
        'category': 'Hoa',
        'childrent': 'Hoa tien',
    },
    {
        'category': 'Hop qua',
        'childrent': 'Socola',
    },
    {
        'category': 'Hop qua',
        'childrent': 'My pham',
    },
    {
        'category': 'BeautyProduct',
        'childrent': 'Nail',
    },
    {
        'category': 'BeautyProduct',
        'childrent': 'Son',
    },
    {
        'category': 'Blog',
        'childrent': 'Qua tang',
    },
    {
        'category': 'Blog',
        'childrent': 'Beautyful',
    },
    {
        'category': 'Blog',
        'childrent': 'CheckGenuine',
    },
]


datas = [
    {
        'name': 'Chuột Mickey',
        'slug': 'chuot-mickey',
        'image': 'https://dn-thumbs.imagevenue.com/de/75/f8/ME15J0OQ_t.jpg',
        'discription': 'Chuột Mickey dáng đứng,  mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 75,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hoat hinh'

    },
    {
        'name': 'Đôrêmon',
        'slug': 'doremon',
        'image': 'https://cdn-thumbs.imagevenue.com/05/4e/85/ME15J0OR_t.jpg',
        'discription': 'Đôrêmon mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 87,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hoat hinh'
    },
    {
        'name': 'Gấu bông lông đỏ',
        'slug': 'gau-bong-long-do',
        'image': 'https://cdn-thumbs.imagevenue.com/7d/f5/18/ME15J0OS_t.jpg',
        'discription': 'Gấu bông lông đỏ dáng đứng , mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 62,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Gau bong',
    },
    {
        'name': 'Gấu bông lông nâu',
        'slug': 'gau-bong-long-nau',
        'image': 'https://cdn-thumbs.imagevenue.com/4a/48/b5/ME15J0OT_t.jpg',
        'discription': 'Gấu bông lông nâu dáng đứng, mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 77,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Gau bong',
    },
    {
        'name': 'Gấu bông lông trắng',
        'slug': 'gau-bong-long-trang',
        'image': 'https://cdn-thumbs.imagevenue.com/1c/76/cc/ME15J0OU_t.jpg',
        'discription': 'Gấu bông lông trắng dáng đứng, mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 76,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Gau bong',
    },
    {
        'name': 'Gấu trúc ngồi',
        'slug': 'gau-truc-ngoi',
        'image': 'https://cdn-thumbs.imagevenue.com/ee/3f/70/ME15J0OW_t.jpg',
        'discription': 'Gấu trúc ngồi dáng đứng, mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 56,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Gau bong',
    },
    {
        'name': 'Teddy đeo tim thêu love',
        'slug': 'teddy-deo-tim-theu-love',
        'image': 'https://cdn-thumbs.imagevenue.com/e7/21/16/ME15J0OV_t.jpg',
        'discription': 'Teddy đeo tim thêu love dáng đứng, mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 67,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Gau bong',
    },
    {
        'name': 'Hổ nằm',
        'slug': 'ho-nam',
        'image': 'https://cdn-thumbs.imagevenue.com/98/f2/e9/ME15J0P9_t.jpg',
        'discription': 'Hổ nằm mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Thu bong',
    },

    {
        'name': 'Hổ ngồi',
        'slug': 'ho-ngoi',
        'image': 'https://cdn-thumbs.imagevenue.com/82/df/94/ME15J0PA_t.jpg',
        'discription': 'hổ ngồi mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Thu bong',
    },
    {
        'name': 'Khủng long nằm',
        'slug': 'khung-long-nam',
        'image': 'https://cdn-thumbs.imagevenue.com/66/55/12/ME15J0Q0_t.jpg',
        'discription': 'Khủng long nằm mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 42,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Thu bong',
    },
    {
        'name': 'Khủng long ngồi',
        'slug': 'khung-long-ngoi',
        'image': 'https://cdn-thumbs.imagevenue.com/ea/ae/ff/ME15J0Q2_t.jpg',
        'discription': 'Khủng long ngồi mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 90,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Thu bong',
    },
    {
        'name': 'Kỳ lân',
        'slug': 'ky-lan',
        'image': 'https://cdn-thumbs.imagevenue.com/c8/81/68/ME15J0Q3_t.jpg',
        'discription': 'Kỳ lân mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Thu bong',
    },
    {
        'name': 'Heo đeo tim',
        'slug': 'heo-deo-tim',
        'image': 'https://cdn-thumbs.imagevenue.com/2f/e1/ac/ME15J0Q4_t.jpg',
        'discription': 'Heo đeo tim mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Thu bong',
    },
    {
        'name': 'Heo Mắt Hồng',
        'slug': 'heo-mat-hong',
        'image': 'https://cdn-thumbs.imagevenue.com/da/de/3f/ME15J0Q5_t.jpg',
        'discription': 'Heo Mắt Hồng mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 24,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Thu bong',
    },
    {
        'name': 'Heo Nằm Mềm',
        'slug': 'heo-nam-mem',
        'image': 'https://cdn-thumbs.imagevenue.com/9b/9a/ad/ME15J0Q7_t.jpg',
        'discription': 'Heo Nằm Mềm mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 65,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Thu bong',
    },
    {
        'name': 'Heo Ong Nằm',
        'slug': 'heo-ong-nam',
        'image': 'https://cdn-thumbs.imagevenue.com/49/9e/a6/ME15J0Q8_t.jpg',
        'discription': 'Heo Ong Nằm mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 78,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Thu bong',
    },

    {
        'name': 'Mèo Hoàng Thượng Ngồi',
        'slug': 'meo-hoang-thuong-ngoi',
        'image': 'https://cdn-thumbs.imagevenue.com/18/f0/1b/ME15J0Q9_t.jpg',
        'discription': 'Mèo hoàng thượng Ngồi mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 78,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Thu bong',
    },
    {
        'name': 'Picachu',
        'slug': 'picachu',
        'image': 'https://cdn-thumbs.imagevenue.com/dc/94/e7/ME15J0QL_t.jpg',
        'discription': 'Picachu mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 78,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hoat hinh'
    },
    {
        'name': 'Picachu Nằm',
        'slug': 'picachu-nam',
        'image': 'https://cdn-thumbs.imagevenue.com/ee/3d/bb/ME15J0QM_t.jpg',
        'discription': 'Picachu Nằm mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 78,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hoat hinh'
    },
    {
        'name': 'Sao ngũ sắc',
        'slug': 'sao-ngu-sac',
        'image': 'https://cdn-thumbs.imagevenue.com/03/9b/69/ME15J0QN_t.jpg',
        'discription': 'Sao ngũ sắc mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 78,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Thu bong',
    },
    {
        'name': 'Thỏ bình sữa',
        'slug': 'tho-binh-sua',
        'image': 'https://cdn-thumbs.imagevenue.com/2e/c7/b1/ME15J0QO_t.jpg',
        'discription': 'Thỏ bình sữa mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 78,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Thu bong',
    },
    {
        'name': 'Vịt bình sữa',
        'slug': 'vit-binh-sua',
        'image': 'https://cdn-thumbs.imagevenue.com/fa/c4/fe/ME15J0QP_t.jpg',
        'discription': 'Vịt bình sữa mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 78,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Thu bong',
    },




    {
        'name': 'Gối ôm bé sâu',
        'slug': 'goi-om-be-sau',
        'image': 'https://cdn-thumbs.imagevenue.com/5f/ee/aa/ME15J0OX_t.jpg',
        'discription': 'Gối ôm hình bé sâu với kiểu dáng thuôn dài, chất nhung bên ngoài siêu mềm mịn kết hợp với chất bông đàn hồi cực kì an toàn là sự lựa chọn lí tưởng cho giấc ngủ của bạn. Đặc biệt gối ôm có nhiều hình, kiểu dáng, màu sắc đa dạng cho bạn thỏa sức lựa chọn',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 81,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Goi bong',
    },
    {
        'name': 'Gối ôm bò sữa',
        'slug': 'goi-om-bo-sua',
        'image': 'https://cdn-thumbs.imagevenue.com/5a/43/bd/ME15J0OY_t.jpg',
        'discription': 'Gối ôm hình bò sữa với kiểu dáng thuôn dài, chất nhung bên ngoài siêu mềm mịn kết hợp với chất bông đàn hồi cực kì an toàn là sự lựa chọn lí tưởng cho giấc ngủ của bạn. Đặc biệt gối ôm có nhiều hình, kiểu dáng, màu sắc đa dạng cho bạn thỏa sức lựa chọn',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 84,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Goi bong',
    },
    {
        'name': 'Gối ôm Chó husky',
        'slug': 'goi-om-cho-husky',
        'image': 'https://cdn-thumbs.imagevenue.com/7c/6a/aa/ME15J0OZ_t.jpg',
        'discription': 'Gối ôm hình Chó husky với kiểu dáng thuôn dài, chất nhung bên ngoài siêu mềm mịn kết hợp với chất bông đàn hồi cực kì an toàn là sự lựa chọn lí tưởng cho giấc ngủ của bạn. Đặc biệt gối ôm có nhiều hình, kiểu dáng, màu sắc đa dạng cho bạn thỏa sức lựa chọn',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 84,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Goi bong',
    },
    {
        'name': 'Gối ôm Chó Vàng',
        'slug': 'goi-om-cho-vang',
        'image': 'https://cdn-thumbs.imagevenue.com/ea/82/02/ME15J0P0_t.jpg',
        'discription': 'Gối ôm hình Chó Vàng với kiểu dáng thuôn dài, chất nhung bên ngoài siêu mềm mịn kết hợp với chất bông đàn hồi cực kì an toàn là sự lựa chọn lí tưởng cho giấc ngủ của bạn. Đặc biệt gối ôm có nhiều hình, kiểu dáng, màu sắc đa dạng cho bạn thỏa sức lựa chọn',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 44,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Goi bong',
    },
    {
        'name': 'Gối ôm mèo hoàng thượng',
        'slug': 'goi-om-meo-hoang-thuong',
        'image': 'https://cdn-thumbs.imagevenue.com/28/61/07/ME15J0P1_t.jpg',
        'discription': 'Gối ôm hình mèo hoàng thượng với kiểu dáng thuôn dài, chất nhung bên ngoài siêu mềm mịn kết hợp với chất bông đàn hồi cực kì an toàn là sự lựa chọn lí tưởng cho giấc ngủ của bạn. Đặc biệt gối ôm có nhiều hình, kiểu dáng, màu sắc đa dạng cho bạn thỏa sức lựa chọn',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 74,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Goi bong',
    },

    {
        'name': 'Gối ôm thú mềm',
        'slug': 'goi-om-thu-mem',
        'image': 'https://cdn-thumbs.imagevenue.com/37/8b/ff/ME15J0P2_t.jpg',
        'discription': 'Gối ôm hình thú với kiểu dáng thuôn dài, chất nhung bên ngoài siêu mềm mịn kết hợp với chất bông đàn hồi cực kì an toàn là sự lựa chọn lí tưởng cho giấc ngủ của bạn. Đặc biệt gối ôm có nhiều hình, kiểu dáng, màu sắc đa dạng cho bạn thỏa sức lựa chọn',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 181,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Goi bong',
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 01',
        'slug': 'hoa-hong-sap-mau-01',
        'image': 'https://cdn-thumbs.imagevenue.com/6d/a8/bb/ME15J0PB_t.jpg',
        'discription': 'Bó Hoa hồng Sáp, số lượng 1 bông, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 382,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hong sap',
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 02',
        'slug': 'hoa-hong-sap-mau-02',
        'image': 'https://cdn-thumbs.imagevenue.com/c6/52/c4/ME15J0PC_t.jpg',
        'discription': 'Bó Hoa hồng Sáp, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 143,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hong sap',
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 03',
        'slug': 'hoa-hong-sap-mau-03',
        'image': 'https://cdn-thumbs.imagevenue.com/18/4c/16/ME15J0PD_t.jpg',
        'discription': 'Bó Hoa hồng Sáp, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 182,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hong sap',
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 04',
        'slug': 'hoa-hong-sap-mau-04',
        'image': 'https://cdn-thumbs.imagevenue.com/0c/5d/1e/ME15J0PE_t.jpg',
        'discription': 'Bó Hoa hồng Sáp, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 42,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hong sap',
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 05',
        'slug': 'hoa-hong-sap-mau-05',
        'image': 'https://cdn-thumbs.imagevenue.com/7c/c6/b0/ME15J0PF_t.jpg',
        'discription': 'Bó Hoa hồng Sáp, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 72,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hong sap',
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 06',
        'slug': 'hoa-hong-sap-mau-06',
        'image': 'https://cdn-thumbs.imagevenue.com/66/6c/4a/ME15J0PG_t.jpg',
        'discription': 'Bó Hoa hồng Sáp, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 142,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hong sap',
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 07',
        'slug': 'hoa-hong-sap-mau-07',
        'image': 'https://cdn-thumbs.imagevenue.com/8e/dc/1e/ME15J0PH_t.jpg',
        'discription': 'Bó Hoa hồng Sáp, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 162,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hong sap',
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 08',
        'slug': 'hoa-hong-sap-mau-08',
        'image': 'https://cdn-thumbs.imagevenue.com/57/f0/ad/ME15J0PI_t.jpg',
        'discription': 'Bó Hoa hồng Sáp, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 165,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hong sap',
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 09',
        'slug': 'hoa-hong-sap-mau-09',
        'image': 'https://cdn-thumbs.imagevenue.com/d3/a8/0b/ME15J0PJ_t.jpg',
        'discription': 'Bó Hoa hồng Sáp, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 157,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hong sap',
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 10',
        'slug': 'hoa-hong-sap-mau-010',
        'image': 'https://cdn-thumbs.imagevenue.com/41/6b/f3/ME15J0PK_t.jpg',
        'discription': 'Bó Hoa hồng Sáp, có kết hợp với đèn nháy tạo điểm nhấn, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hong sap',
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 11',
        'slug': 'hoa-hong-sap-mau-011',
        'image': 'https://cdn-thumbs.imagevenue.com/57/92/da/ME15J0PL_t.jpg',
        'discription': 'Bó Hoa hồng Sáp, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 88,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hong sap',
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 12',
        'slug': 'hoa-hong-sap-mau-012',
        'image': 'https://cdn-thumbs.imagevenue.com/7c/fd/b2/ME15J0PM_t.jpg',
        'discription': 'Bó Hoa hồng Sáp, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 93,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hong sap',
    },
    {
        'name': 'Hộp Quà Tình Yêu - Mẫu 01',
        'slug': 'hop-qua-mau-01',
        'image': 'https://cdn-thumbs.imagevenue.com/31/6a/2d/ME15J0PN_t.jpg',
        'discription': 'Hộp quà tặng tình yêu, được kết hợp bởi các món quà chất lượng và trang trí đẹp mắt...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 87,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'My pham',
    },
    {
        'name': 'Hộp Quà Tình Yêu - Mẫu 02',
        'slug': 'hop-qua-mau-02',
        'image': 'https://cdn-thumbs.imagevenue.com/ab/f2/ad/ME15J0PO_t.jpg',
        'discription': 'Hộp quà tặng tình yêu, được kết hợp bởi các món quà chất lượng và trang trí đẹp mắt...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 122,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'My pham',
    },
    {
        'name': 'Hộp Quà Tình Yêu - Mẫu 03',
        'slug': 'hop-qua-mau-03',
        'image': 'https://cdn-thumbs.imagevenue.com/01/ab/79/ME15J0PP_t.jpg',
        'discription': 'Hộp quà tặng tình yêu, được kết hợp bởi các món quà chất lượng và trang trí đẹp mắt...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 66,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'My pham',
    },
    {
        'name': 'Hộp Quà Tình Yêu - Mẫu 04',
        'slug': 'hop-qua-mau-04',
        'image': 'https://cdn-thumbs.imagevenue.com/a2/5c/00/ME15J0PQ_t.jpg',
        'discription': 'Hộp quà tặng tình yêu, được kết hợp bởi các món quà chất lượng và trang trí đẹp mắt...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 165,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'My pham',
    },
    {
        'name': 'Hộp Quà Tình Yêu - Mẫu 05',
        'slug': 'hop-qua-mau-05',
        'image': 'https://cdn-thumbs.imagevenue.com/43/a2/8c/ME15J0PR_t.jpg',
        'discription': 'Hộp quà tặng tình yêu, được kết hợp bởi các món quà chất lượng và trang trí đẹp mắt...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 72,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'My pham',
    },
    {
        'name': 'Hộp Quà Tình Yêu - Mẫu 06',
        'slug': 'hop-qua-mau-06',
        'image': 'https://cdn-thumbs.imagevenue.com/b7/3b/aa/ME15J0PS_t.jpg',
        'discription': 'Hộp quà tặng tình yêu, được kết hợp bởi các món quà chất lượng và trang trí đẹp mắt...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 46,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'My pham',
    },
    {
        'name': 'Hộp Quà Tình Yêu - Mẫu 07',
        'slug': 'hop-qua-mau-07',
        'image': 'https://cdn-thumbs.imagevenue.com/28/52/ae/ME15J0PT_t.jpg',
        'discription': 'Hộp quà tặng tình yêu, được kết hợp bởi các món quà chất lượng và trang trí đẹp mắt...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 165,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'My pham',
    },
    {
        'name': 'Hộp Quà Tình Yêu - Mẫu 08',
        'slug': 'hop-qua-mau-08',
        'image': 'https://cdn-thumbs.imagevenue.com/db/ad/b8/ME15J0PU_t.jpg',
        'discription': 'Hộp quà tặng tình yêu, được kết hợp bởi các món quà chất lượng và trang trí đẹp mắt...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'My pham',
    },
    {
        'name': 'Hộp Quà Socola Tình Yêu - Mẫu 01',
        'slug': 'hop-qua-socola-mau-01',
        'image': 'https://cdn-thumbs.imagevenue.com/73/96/da/ME15J0PV_t.jpg',
        'discription': 'Hộp quà tặng Socola tình yêu, được kết hợp bởi những viên sôcôla thơm ngon chất lượng và trang trí đẹp mắt...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 282,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Socola',
    },
    {
        'name': 'Hộp Quà Socola Tình Yêu - Mẫu 02',
        'slug': 'hop-qua-socola-mau-02',
        'image': 'https://cdn-thumbs.imagevenue.com/91/e1/08/ME15J0PW_t.jpg',
        'discription': 'Hộp quà tặng Socola tình yêu, được kết hợp bởi những viên sôcôla thơm ngon chất lượng và trang trí đẹp mắt...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 142,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Socola',
    },
    {
        'name': 'Hộp Quà Socola Tình Yêu - Mẫu 03',
        'slug': 'hop-qua-socola-mau-03',
        'image': 'https://cdn-thumbs.imagevenue.com/49/d3/d1/ME15J0PX_t.jpg',
        'discription': 'Hộp quà tặng Socola tình yêu, được kết hợp bởi những viên sôcôla thơm ngon chất lượng và trang trí đẹp mắt...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 168,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Socola',
    },
    {
        'name': 'Hộp Quà Socola Tình Yêu - Mẫu 04',
        'slug': 'hop-qua-socola-mau-04',
        'image': 'https://cdn-thumbs.imagevenue.com/54/e3/0c/ME15J0PY_t.jpg',
        'discription': 'Hộp quà tặng Socola tình yêu, được kết hợp bởi những viên sôcôla thơm ngon chất lượng và trang trí đẹp mắt...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 133,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Socola',
    },
    {
        'name': 'Hộp Quà Socola Tình Yêu - Mẫu 05',
        'slug': 'hop-qua-socola-mau-05',
        'image': 'https://cdn-thumbs.imagevenue.com/bb/b4/93/ME15J0PZ_t.jpg',
        'discription': 'Hộp quà tặng Socola tình yêu, được kết hợp bởi những viên sôcôla thơm ngon chất lượng và trang trí đẹp mắt...',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 243,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Socola',
    },
    {
        'name': 'Hoa tiền - Mẫu 01',
        'slug': 'hoa-tien-mau-01',
        'image': 'https://cdn-thumbs.imagevenue.com/53/78/ee/ME15J0P3_t.jpg',
        'discription': 'Bó hoa được kết hợp từ những đồng tiền có mệnh giá theo yêu cầu, là kết hợp của sự lãng mạng và sự khẳng định đẳng cấp',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 246,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hoa tien',
    },
    {
        'name': 'Hoa tiền - Mẫu 02',
        'slug': 'hoa-tien-mau-02',
        'image': 'https://cdn-thumbs.imagevenue.com/bd/7f/5e/ME15J0P4_t.jpg',
        'discription': 'Bó hoa được kết hợp từ những đồng tiền có mệnh giá theo yêu cầu, là kết hợp của sự lãng mạng và sự khẳng định đẳng cấp',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 132,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hoa tien',
    },
    {
        'name': 'Hoa tiền - Mẫu 03',
        'slug': 'hoa-tien-mau-03',
        'image': 'https://cdn-thumbs.imagevenue.com/be/1c/86/ME15J0P5_t.jpg',
        'discription': 'Bó hoa được kết hợp từ những đồng tiền có mệnh giá theo yêu cầu, là kết hợp của sự lãng mạng và sự khẳng định đẳng cấp',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hoa tien',
    },
    {
        'name': 'Hoa tiền - Mẫu 06',
        'slug': 'hoa-tien-mau-06',
        'image': 'https://cdn-thumbs.imagevenue.com/0b/28/35/ME15J0P6_t.jpg',
        'discription': 'Bó hoa được kết hợp từ những đồng tiền có mệnh giá theo yêu cầu, là kết hợp của sự lãng mạng và sự khẳng định đẳng cấp',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hoa tien',
    },
    {
        'name': 'Hoa tiền - Mẫu 07',
        'slug': 'hoa-tien-mau-07',
        'image': 'https://cdn-thumbs.imagevenue.com/4d/63/96/ME15J0P7_t.jpg',
        'discription': 'Bó hoa được kết hợp từ những đồng tiền có mệnh giá theo yêu cầu, là kết hợp của sự lãng mạng và sự khẳng định đẳng cấp',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hoa tien',
    },
    {
        'name': 'Hoa tiền - Mẫu 08',
        'slug': 'hoa-tien-mau-08',
        'image': 'https://cdn-thumbs.imagevenue.com/c9/12/f4/ME15J0P8_t.jpg',
        'discription': 'Bó hoa được kết hợp từ những đồng tiền có mệnh giá theo yêu cầu, là kết hợp của sự lãng mạng và sự khẳng định đẳng cấp',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Hoa tien',
    },

    {
        'name': 'Nail - Mẫu 01 ',
        'slug': 'nail-mau-01',
        'image': 'https://cdn-thumbs.imagevenue.com/e1/b2/d3/ME15J0QB_t.jpg',
        'discription': 'Nail  - những mẫu Nail đẹp .',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 78,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Nail',
    },
    {
        'name': 'Nail - Mẫu 02 ',
        'slug': 'nail-mau-02',
        'image': 'https://cdn-thumbs.imagevenue.com/a7/f3/e4/ME15J0QD_t.jpg',
        'discription': 'Nail  - những mẫu Nail đẹp .',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 78,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Nail',
    },
    {
        'name': 'Nail - Mẫu 03 ',
        'slug': 'nail-mau-03',
        'image': 'https://cdn-thumbs.imagevenue.com/2b/68/ee/ME15J0QE_t.jpg',
        'discription': 'Nail  - những mẫu Nail đẹp .',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 78,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Nail',
    },
    {
        'name': 'Nail - Mẫu 04 ',
        'slug': 'nail-mau-04',
        'image': 'https://cdn-thumbs.imagevenue.com/c6/a5/99/ME15J0QF_t.jpg',
        'discription': 'Nail  - những mẫu Nail đẹp .',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 78,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Nail',
    },
    {
        'name': 'Nail - Mẫu 05 ',
        'slug': 'nail-mau-05',
        'image': 'https://cdn-thumbs.imagevenue.com/65/6c/c5/ME15J0QG_t.jpg',
        'discription': 'Nail  - những mẫu Nail đẹp .',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 78,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Nail',
    },
    {
        'name': 'Nail - Mẫu 06 ',
        'slug': 'nail-mau-06',
        'image': 'https://cdn-thumbs.imagevenue.com/53/85/14/ME15J0QH_t.jpg',
        'discription': 'Nail  - những mẫu Nail đẹp .',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 78,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Nail',
    },

    {
        'name': 'Nail - Mẫu 08 ',
        'slug': 'nail-mau-08',
        'image': 'https://cdn-thumbs.imagevenue.com/d2/26/38/ME15J0QI_t.jpg',
        'discription': 'Nail  - những mẫu Nail đẹp .',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 78,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Nail',
    },
    {
        'name': 'Nail - Mẫu 09 ',
        'slug': 'nail-mau-09',
        'image': 'https://cdn-thumbs.imagevenue.com/48/2c/22/ME15J0QJ_t.jpg',
        'discription': 'Nail  - những mẫu Nail đẹp .',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 78,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Nail',
    },
    {
        'name': 'Nail - Mẫu 07 ',
        'slug': 'nail-mau-07',
        'image': 'https://cdn-thumbs.imagevenue.com/6e/0e/3c/ME15J0QK_t.jpg',
        'discription': 'Nail  - những mẫu Nail đẹp .',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 78,
        'initial_price': 200000,
        'curent_price': 200000,
        'discount_product': False,
        'hot_product': False,
        'childrent_category': 'Nail',
    },



]


# phan trang


class PageSize24Pagiration(PageNumberPagination):
    page_size = 24


class PageSize10Pagiration(PageNumberPagination):
    page_size = 10


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.filter(active=True)
    serializer_class = ProductSerialize


class ProductBestSellerViewSet(viewsets.ViewSet, generics.ListAPIView):

    queryset = Products.objects.filter(active=True)
    queryset = queryset.order_by('-amount_sold')
    serializer_class = ProductSerialize
    pagination_class = PageSize10Pagiration


class NewProductViewSet(viewsets.ViewSet, generics.ListAPIView):

    queryset = Products.objects.filter(active=True)
    queryset = queryset.order_by('-create_date')
    serializer_class = ProductSerialize
    pagination_class = PageSize10Pagiration


class GauBongViewSet(viewsets.ViewSet, generics.ListAPIView):

    queryset = Products.objects.filter(active=True, childrent_category=1)
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class ThuBongViewSet(viewsets.ViewSet, generics.ListAPIView):

    queryset = Products.objects.filter(active=True, childrent_category=2)
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class GoiBongViewSet(viewsets.ViewSet, generics.ListAPIView):

    queryset = Products.objects.filter(active=True, childrent_category=4)
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class GauBongHoatHinhViewSet(viewsets.ViewSet, generics.ListAPIView):

    queryset = Products.objects.filter(active=True, childrent_category=3)
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class BupBeViewSet(viewsets.ViewSet, generics.ListAPIView):

    queryset = Products.objects.filter(active=True, childrent_category=5)
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class HongSapViewSet(viewsets.ViewSet, generics.ListAPIView):

    queryset = Products.objects.filter(active=True, childrent_category=6)
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class HoaTienViewSet(viewsets.ViewSet, generics.ListAPIView):

    queryset = Products.objects.filter(active=True, childrent_category=7)
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class SocolaViewSet(viewsets.ViewSet, generics.ListAPIView):

    queryset = Products.objects.filter(active=True, childrent_category=8)
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class MyPhamViewSet(viewsets.ViewSet, generics.ListAPIView):

    queryset = Products.objects.filter(active=True, childrent_category=9)
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class NailHotViewSet(viewsets.ViewSet, generics.ListAPIView):

    queryset = Products.objects.filter(active=True, childrent_category='10')
    queryset = queryset.order_by('-amount_sold')
    serializer_class = ProductSerialize
    pagination_class = PageSize10Pagiration


class NailViewSet(viewsets.ViewSet, generics.ListAPIView):

    queryset = Products.objects.filter(active=True, childrent_category='10')
    queryset = queryset.order_by('-amount_sold')
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class SonViewSet(viewsets.ViewSet, generics.ListAPIView):

    queryset = Products.objects.filter(active=True, childrent_category='11')
    queryset = queryset.order_by('-amount_sold')
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class QuaTangViewSet(viewsets.ViewSet, generics.ListAPIView):

    queryset = Products.objects.filter(active=True, childrent_category='12')
    queryset = queryset.order_by('-amount_sold')
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class BeautyfulViewSet(viewsets.ViewSet, generics.ListAPIView):

    queryset = Products.objects.filter(active=True, childrent_category='13')
    queryset = queryset.order_by('-amount_sold')
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class CheckGenuineViewSet(viewsets.ViewSet, generics.ListAPIView):

    queryset = Products.objects.filter(active=True, childrent_category='14')
    queryset = queryset.order_by('-amount_sold')
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class TeddyBearHotViewSet(viewsets.ViewSet, generics.ListAPIView):

    queryset = Products.objects.filter(active=True, childrent_category='1')
    queryset = queryset.order_by('-amount_sold')
    serializer_class = ProductSerialize
    pagination_class = PageSize10Pagiration


class BouquetHotViewSet(viewsets.ViewSet, generics.ListAPIView):

    queryset = Products.objects.filter(active=True, childrent_category=6)
    queryset = queryset.order_by('-amount_sold')
    serializer_class = ProductSerialize
    pagination_class = PageSize10Pagiration


class GiftBoxHotViewSet(viewsets.ViewSet, generics.ListAPIView):

    queryset = Products.objects.filter(active=True, childrent_category=9)
    queryset = queryset.order_by('-amount_sold')
    serializer_class = ProductSerialize
    pagination_class = PageSize10Pagiration


class SearchNameListViewSet(viewsets.ViewSet):
    parser_classes = [MultiPartParser, JSONParser, FormParser, ]

    def list(self, request):
        try:

            value = request.query_params.getlist('value')
            page = request.query_params.getlist('page')

            paginator = PageNumberPagination()
            paginator.page_size = 10
            paginator.page_query_param = page[0]
            qry_set = Products.objects.filter(
                active=True, name__icontains=value[0])
            p = paginator.paginate_queryset(
                queryset=qry_set, request=request)  # change 1
            serializer = ProductSerialize(p, many=True)  # change 2
            theData = serializer.data
        except Exception as e:
            return Response({
                'Status': 'Failed',
                'Message': str(e),
            }, status=status.HTTP_400_BAD_REQUEST)

        return paginator.get_paginated_response(theData)  # change 3


# def index(request):
#     for data in CategoryData:
#         if data == 'Gau':
#             gau = Category.objects.get_or_create(name='Gấu')
#         elif data == 'Hoa':
#             hoa = Category.objects.get_or_create(name='Hoa')
#         elif data == 'Hop qua':
#             qua = Category.objects.get_or_create(name='Hộp quà')
#         elif data == 'BeautyProduct':
#             beau = Category.objects.get_or_create(name='BeautyProduct')
#         elif data == 'Blog':
#             blog = Category.objects.get_or_create(name='Blog')


#     for data in childrentCategoryData:
#         if data['category'] == 'Gau':
#             if data['childrent'] == 'Gau bong':
#                 ChildrentCategory.objects.get_or_create(
#                     name='Gấu Bông', category=gau)
#             elif data['childrent'] == 'Thu bong':
#                 ChildrentCategory.objects.get_or_create(
#                     name='Thú Bông', category=gau)
#             elif data['childrent'] == 'Hoat hinh':
#                 ChildrentCategory.objects.get_or_create(
#                     name='Gấu Bông Hoạt Hình', category=gau)
#             elif data['childrent'] == 'Goi bong':
#                 ChildrentCategory.objects.get_or_create(
#                     name='Gối Bông', category=gau)
#             elif data['childrent'] == 'Bup be':
#                 ChildrentCategory.objects.get_or_create(
#                     name='Búp Bê', category=gau)
#         elif data['category'] == 'Hoa':
#             if data['childrent'] == 'Hong sap':
#                 ChildrentCategory.objects.get_or_create(
#                     name='Hồng sáp', category=hoa)
#             elif data['childrent'] == 'Hoa tien':
#                 ChildrentCategory.objects.get_or_create(
#                     name='Hoa tiền', category=hoa)

#         elif data['category'] == 'Hop qua':
#             if data['childrent'] == 'Socola':
#                 ChildrentCategory.objects.get_or_create(
#                     name='Socola', category=qua)
#             elif data['childrent'] == 'My pham':
#                 ChildrentCategory.objects.get_or_create(
#                     name='Mỹ phẩm', category=qua)

#         elif data['category'] == 'BeautyProduct':
#             if data['childrent'] == 'Nail':
#                 ChildrentCategory.objects.get_or_create(
#                     name='Nail', category=beau)
#             elif data['childrent'] == 'Son':
#                 ChildrentCategory.objects.get_or_create(
#                     name='Son', category=beau)

#         elif data['category'] == 'Blog':
#             if data['childrent'] == 'Qua tang':
#                 ChildrentCategory.objects.get_or_create(
#                     name='Quà tặng', category=blog)
#             elif data['childrent'] == 'Beautyful':
#                 ChildrentCategory.objects.get_or_create(
#                     name='Beautyful', category=blog)
#             elif data['childrent'] == 'CheckGenuine':
#                 ChildrentCategory.objects.get_or_create(
#                     name='CheckGenuine', category=blog)

#     for data in datas:
#         if data['childrent_category'] == 'Gau bong':
#             c = ChildrentCategory.objects.get(name='Gấu Bông')
#         elif data['childrent_category'] == 'Thu bong':
#             c = ChildrentCategory.objects.get(name='Thú Bông')
#         elif data['childrent_category'] == 'Hoat hinh':
#             c = ChildrentCategory.objects.get(name='Gấu Bông Hoạt Hình')
#         elif data['childrent_category'] == 'Goi bong':
#             c = ChildrentCategory.objects.get(name='Gối Bông')
#         elif data['childrent_category'] == 'Bup be':
#             c = ChildrentCategory.objects.get(name='Búp Bê')

#         elif data['childrent_category'] == 'Hong sap':
#             c = ChildrentCategory.objects.get(name='Hồng sáp')
#         elif data['childrent_category'] == 'Hoa tien':
#             c = ChildrentCategory.objects.get(name='Hoa tiền')

#         elif data['childrent_category'] == 'Socola':
#             c = ChildrentCategory.objects.get(name='Socola')
#         elif data['childrent_category'] == 'My pham':
#             c = ChildrentCategory.objects.get(name='Mỹ phẩm')

#         elif data['childrent_category'] == 'Nail':
#             c = ChildrentCategory.objects.get(name='Nail')
#         elif data['childrent_category'] == 'Son':
#             c = ChildrentCategory.objects.get(name='Son')

#         elif data['childrent_category'] == 'Qua tang':
#             c = ChildrentCategory.objects.get(name='Quà tặng')
#         elif data['childrent_category'] == 'Beautyful':
#             c = ChildrentCategory.objects.get(name='Beautyful')
#         elif data['childrent_category'] == 'CheckGenuine':
#             c = ChildrentCategory.objects.get(name='CheckGenuine')
#         else:
#             c = ''

#         Products.objects.get_or_create(name=data['name'],  image=data['image'], discription=data['discription'], initial_price=data['initial_price'],
#                                        curent_price=data['curent_price'], discount_product=data['discount_product'], hot_product=data['hot_product'], amount_sold=data['amount_sold'], childrent_category=c)
#     return render(request, template_name='index.html', context={
#         'name': 'tạo database xong'
#     })

    # def index(request):
    #     for data in datas:
    #         pass
    #     return render(request, template_name='index.html', context={
    #         'name': "Django deploy Heroku !!!"
    #     })

    # Create your views here.

    # https://cdn-thumbs.imagevenue.com/de/75/f8/ME15J0OQ_t.jpg
    # https://cdn-thumbs.imagevenue.com/05/4e/85/ME15J0OR_t.jpg
    # https://cdn-thumbs.imagevenue.com/7d/f5/18/ME15J0OS_t.jpg
    # https://cdn-thumbs.imagevenue.com/4a/48/b5/ME15J0OT_t.jpg
    # https://cdn-thumbs.imagevenue.com/1c/76/cc/ME15J0OU_t.jpg
    # https://cdn-thumbs.imagevenue.com/e7/21/16/ME15J0OV_t.jpg
    # https://cdn-thumbs.imagevenue.com/ee/3f/70/ME15J0OW_t.jpg
    # https://cdn-thumbs.imagevenue.com/5f/ee/aa/ME15J0OX_t.jpg
    # https://cdn-thumbs.imagevenue.com/5a/43/bd/ME15J0OY_t.jpg
    # https://cdn-thumbs.imagevenue.com/7c/6a/aa/ME15J0OZ_t.jpg
    # https://cdn-thumbs.imagevenue.com/ea/82/02/ME15J0P0_t.jpg
    # https://cdn-thumbs.imagevenue.com/28/61/07/ME15J0P1_t.jpg
    # https://cdn-thumbs.imagevenue.com/37/8b/ff/ME15J0P2_t.jpg
    # https://cdn-thumbs.imagevenue.com/53/78/ee/ME15J0P3_t.jpg
    # https://cdn-thumbs.imagevenue.com/bd/7f/5e/ME15J0P4_t.jpg
    # https://cdn-thumbs.imagevenue.com/be/1c/86/ME15J0P5_t.jpg
    # https://cdn-thumbs.imagevenue.com/0b/28/35/ME15J0P6_t.jpg
    # https://cdn-thumbs.imagevenue.com/4d/63/96/ME15J0P7_t.jpg
    # https://cdn-thumbs.imagevenue.com/c9/12/f4/ME15J0P8_t.jpg
    # https://cdn-thumbs.imagevenue.com/98/f2/e9/ME15J0P9_t.jpg
    # https://cdn-thumbs.imagevenue.com/82/df/94/ME15J0PA_t.jpg
    # https://cdn-thumbs.imagevenue.com/6d/a8/bb/ME15J0PB_t.jpg
    # https://cdn-thumbs.imagevenue.com/c6/52/c4/ME15J0PC_t.jpg
    # https://cdn-thumbs.imagevenue.com/18/4c/16/ME15J0PD_t.jpg
    # https://cdn-thumbs.imagevenue.com/0c/5d/1e/ME15J0PE_t.jpg
    # https://cdn-thumbs.imagevenue.com/7c/c6/b0/ME15J0PF_t.jpg
    # https://cdn-thumbs.imagevenue.com/66/6c/4a/ME15J0PG_t.jpg
    # https://cdn-thumbs.imagevenue.com/8e/dc/1e/ME15J0PH_t.jpg
    # https://cdn-thumbs.imagevenue.com/57/f0/ad/ME15J0PI_t.jpg
    # https://cdn-thumbs.imagevenue.com/d3/a8/0b/ME15J0PJ_t.jpg
    # https://cdn-thumbs.imagevenue.com/41/6b/f3/ME15J0PK_t.jpg
    # https://cdn-thumbs.imagevenue.com/57/92/da/ME15J0PL_t.jpg
    # https://cdn-thumbs.imagevenue.com/7c/fd/b2/ME15J0PM_t.jpg
    # https://cdn-thumbs.imagevenue.com/31/6a/2d/ME15J0PN_t.jpg
    # https://cdn-thumbs.imagevenue.com/ab/f2/ad/ME15J0PO_t.jpg
    # https://cdn-thumbs.imagevenue.com/01/ab/79/ME15J0PP_t.jpg
    # https://cdn-thumbs.imagevenue.com/a2/5c/00/ME15J0PQ_t.jpg
    # https://cdn-thumbs.imagevenue.com/43/a2/8c/ME15J0PR_t.jpg
    # https://cdn-thumbs.imagevenue.com/b7/3b/aa/ME15J0PS_t.jpg
    # https://cdn-thumbs.imagevenue.com/28/52/ae/ME15J0PT_t.jpg
    # https://cdn-thumbs.imagevenue.com/db/ad/b8/ME15J0PU_t.jpg
    # https://cdn-thumbs.imagevenue.com/73/96/da/ME15J0PV_t.jpg
    # https://cdn-thumbs.imagevenue.com/91/e1/08/ME15J0PW_t.jpg
    # https://cdn-thumbs.imagevenue.com/49/d3/d1/ME15J0PX_t.jpg
    # https://cdn-thumbs.imagevenue.com/54/e3/0c/ME15J0PY_t.jpg
    # https://cdn-thumbs.imagevenue.com/bb/b4/93/ME15J0PZ_t.jpg
    # https://cdn-thumbs.imagevenue.com/66/55/12/ME15J0Q0_t.jpg
    # https://cdn-thumbs.imagevenue.com/08/fa/1c/ME15J0Q1_t.jpg
    # https://cdn-thumbs.imagevenue.com/ea/ae/ff/ME15J0Q2_t.jpg
    # https://cdn-thumbs.imagevenue.com/c8/81/68/ME15J0Q3_t.jpg
    # https://cdn-thumbs.imagevenue.com/2f/e1/ac/ME15J0Q4_t.jpg
    # https://cdn-thumbs.imagevenue.com/da/de/3f/ME15J0Q5_t.jpg
    # https://cdn-thumbs.imagevenue.com/9b/9a/ad/ME15J0Q7_t.jpg
    # https://cdn-thumbs.imagevenue.com/49/9e/a6/ME15J0Q8_t.jpg
    # https://cdn-thumbs.imagevenue.com/18/f0/1b/ME15J0Q9_t.jpg
    # https://cdn-thumbs.imagevenue.com/e1/b2/d3/ME15J0QB_t.jpg
    # https://cdn-thumbs.imagevenue.com/a7/f3/e4/ME15J0QD_t.jpg
    # https://cdn-thumbs.imagevenue.com/2b/68/ee/ME15J0QE_t.jpg
    # https://cdn-thumbs.imagevenue.com/c6/a5/99/ME15J0QF_t.jpg
    # https://cdn-thumbs.imagevenue.com/65/6c/c5/ME15J0QG_t.jpg
    # https://cdn-thumbs.imagevenue.com/53/85/14/ME15J0QH_t.jpg
    # https://cdn-thumbs.imagevenue.com/d2/26/38/ME15J0QI_t.jpg
    # https://cdn-thumbs.imagevenue.com/48/2c/22/ME15J0QJ_t.jpg
    # https://cdn-thumbs.imagevenue.com/6e/0e/3c/ME15J0QK_t.jpg
    # https://cdn-thumbs.imagevenue.com/dc/94/e7/ME15J0QL_t.jpg
    # https://cdn-thumbs.imagevenue.com/ee/3d/bb/ME15J0QM_t.jpg
    # https://cdn-thumbs.imagevenue.com/03/9b/69/ME15J0QN_t.jpg
    # https://cdn-thumbs.imagevenue.com/2e/c7/b1/ME15J0QO_t.jpg
    # https://cdn-thumbs.imagevenue.com/fa/c4/fe/ME15J0QP_t.jpg
