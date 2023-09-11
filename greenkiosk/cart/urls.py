from django.urls import path
from cart.views import add_to_cart, cart_list

urlpatterns = [
    path("cart/upload",add_to_cart,name="add_to_cart"),
    path("cart/list",cart_list,name="cart_list_view"),
    
]
