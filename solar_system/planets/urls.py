from django.urls import path
from . import views 

app_name = "planets"

urlpatterns = [
    path('', views.home, name='home'),
    path('star/', views.star_detail, name='star_detail'),
    
    # Endpoint JSON para cargar dinámicamente datos de planetas vía fetch() sin recargar la página.
    path("api/planet/<slug:slug>/", views.planet_data)
]