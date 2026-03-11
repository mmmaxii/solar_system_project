from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "planets/home.html")

#creamos un request para el caso que queramos el url del sol
def star_detail(request):
    return render(request, "planets/star.html")

#tambien creamos un request para ver los url de los planetas
def planet_detail(request, name):
    return render(request, "planets/planet.html", {"name": name})