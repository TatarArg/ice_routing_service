from rest_framework import serializers
from .models import Ship, ShipPosition, WaterArea, WaterAreaPoint


class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = ("id", "mmsi", "name")


class WaterAreaPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterAreaPoint
        fields = ("id", "latitude", "longitude", "order")


class WaterAreaSerializer(serializers.ModelSerializer):
    points = WaterAreaPointSerializer(many=True, read_only=True)

    class Meta:
        model = WaterArea
        fields = ("id", "name", "lat_min", "lat_max", "lon_min", "lon_max", "points")


class WaterAreaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterArea
        fields = ("id", "name", "lat_min", "lat_max", "lon_min", "lon_max")