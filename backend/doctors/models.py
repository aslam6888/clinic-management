from django.db import models
from django.contrib.auth.models import User
# Create your models here.

GENDER = (('male', 'Male'), ('female', 'Female'), ('others', 'Others'))

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    gender = models.CharField(max_length=100, choices=GENDER)
    department = models.ForeignKey("Department", on_delete=models.SET_NULL, null=True)
    dob = models.DateField(null=False, blank=False)
    phone_number = models.CharField(max_length=10)
    qualification = models.CharField(max_length=100, null=False, blank=False)
    licence_number = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.user.username

class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name