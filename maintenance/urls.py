# from django.urls import path # type: ignore
from . import views

from rest_framework.routers import DefaultRouter # type: ignore
from .views import *

router = DefaultRouter()
router.register('assets', AssetViewSet, basename='asset')
router.register('records', MaintenanceRecordViewSet, basename='record')
router.register('schedules', ScheduleViewSet, basename='schedule')


urlpatterns = router.urls