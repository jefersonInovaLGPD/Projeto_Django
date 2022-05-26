from email.policy import default
from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_razao_social = models.CharField(max_length=100)
    customer_cnpj = models.CharField(max_length=18)
    customer_fantasy_name = models.CharField(max_length=100)
    customer_contact_name = models.CharField(max_length=50, blank=True)
    customer_contact_email = models.EmailField(max_length=300, blank=True)
    customer_logo = models.ImageField(upload_to='media/logos', blank=True, default = '')

