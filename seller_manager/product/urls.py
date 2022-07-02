from django.urls import path

from product.views import detail, product_list
from . import views

urlpatterns = [
    path('product/<int:id>', detail, name="detail"),
    path('products', product_list, name="products")
]
