from rest_framework import viewsets
from .models import Ship, WaterArea, WaterAreaPoint, IceZone
from .serializers import ShipSerializer, WaterAreaSerializer, WaterAreaCreateSerializer, WaterAreaPointSerializer, IceZoneSerializer


class ShipViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer


class WaterAreaViewSet(viewsets.ModelViewSet):
    queryset = WaterArea.objects.prefetch_related("points", "ice_zones").all()

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return WaterAreaCreateSerializer
        return WaterAreaSerializer


class WaterAreaPointViewSet(viewsets.ModelViewSet):
    queryset = WaterAreaPoint.objects.all()
    serializer_class = WaterAreaPointSerializer


class IceZoneViewSet(viewsets.ModelViewSet):
    queryset = IceZone.objects.all()
    serializer_class = IceZoneSerializer