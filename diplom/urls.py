from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import ShipViewSet, WaterAreaViewSet, WaterAreaPointViewSet

router = DefaultRouter()
router.register(r'ships', ShipViewSet)
router.register(r'areas', WaterAreaViewSet)
router.register(r'area-points', WaterAreaPointViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]