from django.db import models

class Planet(models.Model):

    # CharField para nombres cortos; SlugField genera URLs amigables (ej: /api/planet/saturn/)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    radius = models.FloatField()
    distance_from_sun = models.FloatField()
    orbital_period = models.FloatField()

    description = models.TextField()

    # Representación en el panel administrativo de Django
    def __str__(self):
        return self.name