from django.urls import path
# from django.conf.urls.static import static
from.views import create_payment


urlpatterns =[
    path("payments/upload",create_payment,name="create_payment_view"),
]
