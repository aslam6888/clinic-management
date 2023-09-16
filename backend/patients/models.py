from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email =  models.CharField(max_length=100)
    gender = models.CharField(max_length=100, null=False, blank=False)
    dob = models.DateField(null=False, blank=False)
    area = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=10)
