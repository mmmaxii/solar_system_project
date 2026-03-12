from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Planet

# Vista principal de la aplicación (Renderiza el entorno 3D)
def home(request):
    return render(request, "planets/home.html")

# Vista dedicada para el componente interactivo del sol
def star_detail(request):
    return render(request, "planets/star.html")


# API Endpoint: Retorna datos serializados de un modelo Planeta específico.
# Útil para inyectar contenido asíncronamente en las tarjetas interactivas (Glassmorphism).
def planet_data(request, slug):

    planet = get_object_or_404(Planet, slug=slug)

    return JsonResponse({
        "name": planet.name,
        "radius": planet.radius,
        "distance": planet.distance_from_sun,
        "orbital_period": planet.orbital_period,
        "description": planet.description
    })