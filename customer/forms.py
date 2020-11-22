from django import forms
from .models import Customer
from django.db import models


class DateInput(forms.DateInput):
    input_type = "date"


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    birth_date = forms.DateField(widget=DateInput())
    area_code = forms.CharField()
    phone_number = forms.CharField()
    country = forms.CharField()
    state = forms.CharField()
    city = forms.CharField()

    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "area_code",
            "phone_number",
            "country",
            "state",
            "city",
        )
