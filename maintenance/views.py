from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

# from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action 
from rest_framework.response import Response
from datetime import date


# Create your views here.
class AssetViewSet(ModelViewSet):
    serializer_class = AssetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): #type : ignore
        return Asset.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False)
    def due(self, request):
        assets = Asset.objects.filter(
            maintenanceschedule__next_service_date__lte=date.today(),
            owner=request.user
        )
        serializers = self.get_serializer(assets, many=True)
        return Response(serializers.data)
        

class MaintenanceRecordViewSet(ModelViewSet):
    serializer_class = MaintenanceRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): #type : ignore
        return MaintenanceRecord.objects.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ScheduleViewSet(ModelViewSet):
    serializer_class = MaintenanceScheduleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MaintenanceSchedule.objects.filter(asset__owner=self.request.user)

    # queryset = MaintenanceSchedule.objects.all()
    
