from django.urls import path
from vendor.views import vendor_registration
urlpatterns = [
    path("vendors/registration",vendor_registration,name="vendor_onboard_view"),
]
