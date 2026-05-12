from rest_framework import serializers
from .models import Ship, WaterArea, WaterAreaPoint, IceCondition, ShipType, IceImpact


class IceImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = IceImpact
        fields = ("id", "ice_type", "coefficient")


class ShipTypeSerializer(serializers.ModelSerializer):
    impacts = IceImpactSerializer(many=True, read_only=True)

    class Meta:
        model = ShipType
        fields = ("id", "code", "impacts")


class ShipSerializer(serializers.ModelSerializer):
    ship_type = ShipTypeSerializer(read_only=True)
    ship_type_id = serializers.PrimaryKeyRelatedField(
        queryset=ShipType.objects.all(), source="ship_type", write_only=True, required=False
    )

    class Meta:
        model = Ship
        fields = ("id", "mmsi", "name", "ship_type", "ship_type_id")


class WaterAreaPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterAreaPoint
        fields = ("id", "area", "latitude", "longitude", "order")


class IceConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IceCondition
        fields = ("id", "area", "ice_type", "lat_min", "lat_max", "lon_min", "lon_max")


class WaterAreaSerializer(serializers.ModelSerializer):
    points = WaterAreaPointSerializer(many=True, read_only=True)
    ice_conditions = IceConditionSerializer(many=True, read_only=True)

    class Meta:
        model = WaterArea
        fields = ("id", "name", "lat_min", "lat_max", "lon_min", "lon_max", "points", "ice_conditions")


class WaterAreaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterArea
        fields = ("id", "name", "lat_min", "lat_max", "lon_min", "lon_max")