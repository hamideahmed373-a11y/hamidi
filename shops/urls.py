from.views import *
from django.urls import path
#from .views import product_details , shop_details

urlpatterns = [
    path('',home,name='home'),
    path('products', all_product, name='products'),
    path('hello', all_shop, name='shops'),
    path('seller',base,name='seller'),
    path('sell', product_page),
    path('details/<int:productid>', product_details, name='search'),
    path('detail/<int:shopid>', shop_details, name='name'),
    path('how',how,name='how'),
    path('ads.txt',ads_txt_view),
]