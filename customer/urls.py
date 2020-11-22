from django.urls import path
from .views import CustumerListView, CustumerCreateView

app_name = "customer"
urlpatterns = [
    path("list/", CustumerListView.as_view(), name="customer-list"),
    path("", CustumerCreateView.as_view(), name="customer-create")
]