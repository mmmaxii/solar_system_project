from django.urls import path
from . import views 

app_name = "planets"

urlpatterns = [
    path('', views.home, name='home'),
    path('star/', views.star_detail, name='star_detail'),
    path("api/planet/<slug:slug>/", views.planet_data)
]