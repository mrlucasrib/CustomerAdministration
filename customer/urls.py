from django.urls import path
from .views import CustumerListView

app_name = "customer"
urlpatterns = [
    path("list/", CustumerListView.as_view(), name="customer-list")
]