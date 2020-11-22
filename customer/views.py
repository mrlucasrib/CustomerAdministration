from django.views.generic import ListView
from .models import Customer
# Create your views here.
class CustumerListView(ListView):
    template_name = "customer/customer_list.html"
    model = Customer
    queryset = Customer.objects.all()
