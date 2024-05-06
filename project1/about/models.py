from django.db import models

# Create your models here.


class Infos(models.Model):
    DISPONIBILITY_CHOICES = (
        ("available","available"),
        ("unavailable","unavailable"),
    )
    description = models.TextField()
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=400)
    birthday = models.DateField()
    website = models.URLField()
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=200)
    age = models.IntegerField()
    degree = models.CharField(max_length=40)
    email = models.EmailField()
    disponibility = models.CharField(max_length=11, choices=DISPONIBILITY_CHOICES)
    details = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='images/')
