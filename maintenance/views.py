from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import MaintenanceRecord
from .serializers import MaintenanceRecordSerializer, MaintenanceScheduleSerializer, AssetSerializer

class MaintenanceRecordList(generics.ListCreateAPIView):
    queryset = MaintenanceRecord.objects.all()
    serializer_class = MaintenanceRecordSerializer
    def perform_create(self, serializer):
        # Custom logic before creating a maintenance record
        serializer.save()

class MaintenanceRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceRecord.objects.all()
    serializer_class = MaintenanceRecordSerializer

    def perform_update(self, serializer):
        # Custom logic before updating a maintenance record
        serializer.save()
