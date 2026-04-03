import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'solar_system.settings')
django.setup()

from planets.models import Planet

data = {
    'mercury': {'mass': 0.055, 'temp': '167 °C'},
    'venus': {'mass': 0.815, 'temp': '464 °C'},
    'earth': {'mass': 1.000, 'temp': '15 °C'},
    'mars': {'mass': 0.107, 'temp': '-65 °C'},
    'jupiter': {'mass': 317.8, 'temp': '-110 °C'},
    'saturn': {'mass': 95.16, 'temp': '-140 °C'},
    'uranus': {'mass': 14.54, 'temp': '-195 °C'},
    'neptune': {'mass': 17.15, 'temp': '-200 °C'}
}

for slug, info in data.items():
    try:
        p = Planet.objects.get(slug=slug)
        p.mass_earth = info['mass']
        p.temperature = info['temp']
        p.save()
        print(f"Updated {slug}")
    except Planet.DoesNotExist:
        print(f"Planet {slug} not found")
