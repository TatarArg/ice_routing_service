from django.contrib import admin
from .models import Ship, ShipPosition


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