from django.db import models

# Create your models here.
class post (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image_url = models.CharField(max_length=100)

class author (models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()