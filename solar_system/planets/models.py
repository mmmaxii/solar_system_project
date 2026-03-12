from django.db import models

class Planet(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    radius = models.FloatField()
    distance_from_sun = models.FloatField()
    orbital_period = models.FloatField()

    description = models.TextField()

    def __str__(self):
        return self.name