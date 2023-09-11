from django .urls import path
from .views import basket_list, create_basket

urlpatterns = [
    path("baskets/form",create_basket,name="create_basket_view"),
    path("basket/list",basket_list,name="basket_list_view"),
]
