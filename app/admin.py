from django.contrib import admin
from .models import Ship, ShipPosition, WaterArea, WaterAreaPoint, IceZone


class ShipPositionInline(admin.TabularInline):
    model = ShipPosition
    extra = 0
    readonly_fields = ("time", "latitude", "longitude", "speed")


@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    list_display = ("mmsi", "name")
    search_fields = ("mmsi", "name")
    inlines = [ShipPositionInline]


@admin.register(ShipPosition)
class ShipPositionAdmin(admin.ModelAdmin):
    list_display = ("ship", "time", "latitude", "longitude", "speed")
    list_filter = ("ship",)


class WaterAreaPointInline(admin.TabularInline):
    model = WaterAreaPoint
    extra = 0


class IceZoneInline(admin.TabularInline):
    model = IceZone
    extra = 0


@admin.register(WaterArea)
class WaterAreaAdmin(admin.ModelAdmin):
    list_display = ("name", "lat_min", "lat_max", "lon_min", "lon_max")
    inlines = [WaterAreaPointInline, IceZoneInline]


@admin.register(IceZone)
class IceZoneAdmin(admin.ModelAdmin):
    list_display = ("area", "ice_type", "lat_min", "lat_max", "lon_min", "lon_max")
    list_filter = ("ice_type",)