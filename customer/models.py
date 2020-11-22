from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    birth_date = models.DateField()
    area_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=9)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        db_table = "customer"