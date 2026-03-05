from django.db import models


class Ship(models.Model):
    mmsi = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name or f"MMSI {self.mmsi}"


class ShipPosition(models.Model):
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE, related_name="positions")
    time = models.DateTimeField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    speed = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = ("ship", "time")

    def __str__(self):
        return f"{self.ship.mmsi} @ {self.time}"