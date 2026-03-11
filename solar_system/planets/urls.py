from django.urls import path
from . import views 

app_name = "planets"

urlpatterns = [
    path('', views.home, name='home'),
    path('star/', views.star_detail, name='star_detail'),
    path('planet/<str:name>/', views.planet_detail, name='planet_detail'), #agregamos los path para la info de los planetas.
]