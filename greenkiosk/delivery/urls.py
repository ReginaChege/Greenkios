from django.urls import path
from delivery.views import delivery_list, place_delivery

urlpatterns = [
    path('delivery/upload', place_delivery, name='place_delivery_view'),
    path("delivery/list",delivery_list,name="delivery_list_view"),
]
