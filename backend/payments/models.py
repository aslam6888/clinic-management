from django.db import models
from patients.models import Patient
# Create your models here.

class Payments(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    total = models.FloatField()
    date_time = models.DateTimeField(auto_now_add=True)