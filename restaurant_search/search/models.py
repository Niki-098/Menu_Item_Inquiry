from django.db import models

# Create your models here.


class Dish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    items = models.TextField()
    lat_long = models.CharField(max_length=100)
    full_details = models.TextField()

    def __str__(self):
        return self.name
