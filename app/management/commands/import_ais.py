import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from app.models import Ship, ShipPosition


class Command(BaseCommand):
    help = 'Import AIS data from CSV'

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str)

    def handle(self, *args, **options):
        filepath = options['filepath']
        created_ships = 0
        created_positions = 0
        skipped = 0

        with open(filepath, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    mmsi = int(row['MMSI'])
                    lat = float(row['LAT'])
                    lon = float(row['LON'])
                    speed = float(row['SOG']) if row.get('SOG') else None
                    time = datetime.strptime(row['BaseDateTime'], '%Y-%m-%dT%H:%M:%S')
                    name = row.get('VesselName', '').strip()

                    ship, created = Ship.objects.get_or_create(mmsi=mmsi, defaults={'name': name})
                    if created:
                        created_ships += 1

                    _, pos_created = ShipPosition.objects.get_or_create(
                        ship=ship,
                        time=time,
                        defaults={
                            'latitude': lat,
                            'longitude': lon,
                            'speed': speed,
                        }
                    )
                    if pos_created:
                        created_positions += 1
                    else:
                        skipped += 1

                except Exception:
                    skipped += 1
                    continue

        self.stdout.write(f"Ships: {created_ships}, Positions: {created_positions}, Skipped: {skipped}")