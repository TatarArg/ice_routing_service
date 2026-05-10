from rest_framework import serializers
from .models import Ship, WaterArea, WaterAreaPoint, IceZone


class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = ("id", "mmsi", "name")


class WaterAreaPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterAreaPoint
        fields = ("id", "area", "latitude", "longitude", "order")


class IceZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = IceZone
        fields = ("id", "area", "ice_type", "lat_min", "lat_max", "lon_min", "lon_max")


class WaterAreaSerializer(serializers.ModelSerializer):
    points = WaterAreaPointSerializer(many=True, read_only=True)
    ice_zones = IceZoneSerializer(many=True, read_only=True)

    class Meta:
        model = WaterArea
        fields = ("id", "name", "lat_min", "lat_max", "lon_min", "lon_max", "points", "ice_zones")


class WaterAreaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterArea
        fields = ("id", "name", "lat_min", "lat_max", "lon_min", "lon_max")