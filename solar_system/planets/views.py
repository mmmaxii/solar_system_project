from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "planets/home.html")

#creamos un request para el caso que queramos el url del sol
def star_detail(request):
    return render(request, "planets/star.html")

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Planet

def planet_data(request, slug):

    planet = get_object_or_404(Planet, slug=slug)

    return JsonResponse({
        "name": planet.name,
        "radius": planet.radius,
        "distance": planet.distance_from_sun,
        "orbital_period": planet.orbital_period,
        "description": planet.description
    })