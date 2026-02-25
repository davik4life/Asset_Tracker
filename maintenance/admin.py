from django.contrib import admin  # type: ignore
from .models import Asset, MaintenanceSchedule, MaintenanceRecord

# Register your models here.
admin.site.register(Asset)
admin.site.register(MaintenanceSchedule)
admin.site.register(MaintenanceRecord)
