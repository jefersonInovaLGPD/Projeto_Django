from django.db import models

# Create your models here.

class Customer(models.Model):
    
    customer_razao_social = models.CharField(max_length=100)
    customer_cnpj = models.CharField(max_length=18)
    customer_fantasy_name = models.CharField(max_length=100)
    customer_contact_name = models.CharField(max_length=50, blank=True)
    customer_contact_email = models.EmailField(max_length=300, blank=True)
    customer_logo = models.ImageField(upload_to='media/logos', blank=True, default = '')

    def __str__(self):
        return self.customer_fantasy_name

class Fases(models.Model):
    step_name = models.CharField(max_length=50)

    def __str__(self):
        return self.step_name

class Tarefas(models.Model):
    task_name = models.CharField(max_length=50)
    task_description = models.CharField(max_length=50)
    task_status = models.CharField(max_length=50)

    def __str__(self):
        return self.task_name

