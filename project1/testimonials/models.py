from django.db import models

# Create your models here.

class Testimonials(models.Model):
    testimonial = models.CharField(max_length=400)
    firstname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    job = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')