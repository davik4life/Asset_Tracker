from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Asset(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    condition = models.CharField(max_length=50)
    purchase_date = models.DateField()

    def __str__(self):
        return self.name
    
class MaintenanceSchedule(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    interval_days = models.IntegerField()
    next_service_date = models.DateField()
    is_active = models.BooleanField(default=True)
class MaintenanceRecord(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    service_date = models.DateField()
    service_type = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True, null=True)
