from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

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

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name','category', 'condition']
    search_fields = ['name', 'category', 'condition']
    ordering_fields = ['name', 'purchase_date', 'created_at']

    def get_queryset(self):
        return Asset.objects.filter(owner=self.request.user)
    
    # def post_queryset(self):
    #     return Asset.objects.filter(owner=self.request.user)
    
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

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['asset__name', 'service_type']
    search_fields = ['asset__name', 'service_type', 'created_by__username']
    ordering_fields = ['service_date', 'cost']

    def get_queryset(self):
        return MaintenanceRecord.objects.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ScheduleViewSet(ModelViewSet):
    serializer_class = MaintenanceScheduleSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['asset__name']
    search_fields = ['asset__name']
    ordering_fields = ['next_service_date', 'interval_days']

    def get_queryset(self):
        return MaintenanceSchedule.objects.filter(asset__owner=self.request.user)
    
