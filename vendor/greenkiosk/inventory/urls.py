from django.urls import path
from django.conf.urls.static import static
from.views import edit_product_view, upload_product,products_list,product_detail,add_to_cart


urlpatterns =[
    path("products/upload",upload_product,name="product-upload_view"),
    path("products/list",products_list,name="products_list_view"),
    path("products/<int:id>/",product_detail,name="product_detail_view"),
    path("products/add_to_cart", add_to_cart, name="add_to_cart_view"),
    path("products/edit/<int:id>/",edit_product_view ,name="edit_product_view"),
]

