from django.contrib import admin
from .models import Ship, ShipPosition, WaterArea, WaterAreaPoint, IceCondition, ShipType, IceImpact


class IceImpactInline(admin.TabularInline):
    model = IceImpact
    extra = 0


@admin.register(ShipType)
class ShipTypeAdmin(admin.ModelAdmin):
    list_display = ["code"]
    inlines = [IceImpactInline]


class ShipPositionInline(admin.TabularInline):
    model = ShipPosition
    extra = 0
    readonly_fields = ("time", "latitude", "longitude", "speed", "course")


@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    list_display = ("mmsi", "name", "ship_type")
    search_fields = ("mmsi", "name")
    inlines = [ShipPositionInline]


@admin.register(ShipPosition)
class ShipPositionAdmin(admin.ModelAdmin):
    list_display = ("ship", "time", "latitude", "longitude", "speed", "course")
    list_filter = ("ship",)


class WaterAreaPointInline(admin.TabularInline):
    model = WaterAreaPoint
    extra = 0


class IceConditionInline(admin.TabularInline):
    model = IceCondition
    extra = 0


@admin.register(WaterArea)
class WaterAreaAdmin(admin.ModelAdmin):
    list_display = ("name", "lat_min", "lat_max", "lon_min", "lon_max")
    inlines = [WaterAreaPointInline, IceConditionInline]


@admin.register(IceCondition)
class IceConditionAdmin(admin.ModelAdmin):
    list_display = ("area", "ice_type", "lat_min", "lat_max", "lon_min", "lon_max")
    list_filter = ("ice_type",)