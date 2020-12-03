from django.db import models


# Create your models here.
class Case(models.Model):
    producent = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    price = models.CharField(max_length=5)

    def __str__(self):
        return self.producent
