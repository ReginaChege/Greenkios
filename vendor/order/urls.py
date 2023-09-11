
from django.urls import path
from .views import order_list, place_order

urlpatterns = [
    path("orders/upload", place_order,name="place_order_views"),
    path("orders/list",order_list,name="order_list_views"),
]
