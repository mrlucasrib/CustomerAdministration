from django.views.generic import ListView, CreateView
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse
# Create your views here.
class CustumerListView(ListView):
    template_name = "customer/customer_list.html"
    model = Customer
    queryset = Customer.objects.all()

class CustumerCreateView(CreateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("customer:customer-list")