from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Q
# Create your views here.


class CustomerListView(ListView):
    template_name = "customer/customer_list.html"
    model = Customer
    paginate_by = 2
    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            object_list = self.model.objects.filter(
                Q(first_name__icontains=name) | Q(last_name__icontains=name)
                )
        else:
            object_list = self.model.objects.all()
        return object_list 


class CustomerCreateView(CreateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("customer:customer-list")


class CustomerUpdateView(UpdateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("customer:customer-list")

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return get_object_or_404(Customer, id=id)


class CustomerDeleteView(DeleteView):
    def get_success_url(self):
        return reverse("customer:customer-list")

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return get_object_or_404(Customer, id=id)
