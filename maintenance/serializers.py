from rest_framework import serializers
from .models import Asset, MaintenanceRecord, MaintenanceSchedule

class AssetSerializer(serializers.ModelSerializer): # Inherit from Serializer here
    class Meta: # Inherit from Meta here
        model = Asset
        fields = '__all__'
        read_only_fields = ["owner"]

class MaintenanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRecord
        fields = '__all__'
        read_only_fields = ["created_by"]

class MaintenanceScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceSchedule
        fields = '__all__'