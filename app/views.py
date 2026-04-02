from rest_framework import viewsets
from rest_framework.response import Response
from .models import Ship, WaterArea, WaterAreaPoint
from .serializers import ShipSerializer, WaterAreaSerializer, WaterAreaCreateSerializer, WaterAreaPointSerializer


class ShipViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer


class WaterAreaViewSet(viewsets.ModelViewSet):
    queryset = WaterArea.objects.prefetch_related("points").all()

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return WaterAreaCreateSerializer
        return WaterAreaSerializer


class WaterAreaPointViewSet(viewsets.ModelViewSet):
    queryset = WaterAreaPoint.objects.all()
    serializer_class = WaterAreaPointSerializer