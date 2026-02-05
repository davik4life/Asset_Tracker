from django.urls import path
from . import views

urlpatterns = [
    path('records/', views.MaintenanceRecordList.as_view(), name='maintenance-record-list'),
    path('records/<int:pk>/', views.MaintenanceRecordDetail.as_view(), name='maintenance-record-detail'),
]