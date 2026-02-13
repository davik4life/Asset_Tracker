from rest_framework import serializers
from .models import Asset, MaintenanceRecord, MaintenanceSchedule
from typing import ClassVar


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model: ClassVar[type] = Asset
        fields: ClassVar[str]= '__all__'
        read_only_fields: ClassVar[list[str]] = ["owner"]


class MaintenanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRecord
        fields = '__all__'
        read_only_fields = ["created_by"]

class MaintenanceScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceSchedule
        fields = '__all__'