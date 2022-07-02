from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    Image = models.ImageField()
    description = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.name}"
