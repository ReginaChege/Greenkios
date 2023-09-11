from django.urls import path
from .views import customer_detail, customer_list, edit_customer_view, upload_customers

app_name = 'customer'

urlpatterns = [
     path("customers/upload",upload_customers,name="customer_upload_view"),
     path("customers/list",customer_list,name="customer_list_view"),
     path("customers/<int:user_id>/",customer_detail,name="customer_detail_view"),
     path("customers/edit/<int:user_id>/",edit_customer_view,name="edit_customer_view"),
      
]