from django.db import models

# Create your models here.
class MovieData(models.Model):
    moviename = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    release_date = models.DateField(null=True, blank=True)
    budget = models.CharField(max_length=30)
    
    def __str__(self):
        return self.moviename