from django.db import models

# Create your models here.

class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    categorie = models.CharField(max_length=50)
    description = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')