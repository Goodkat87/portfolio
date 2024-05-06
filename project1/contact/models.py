from django.db import models

# Create your models here.


class Contact(models.Model):
    description = models.CharField(max_length=400)
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    locality = models.CharField(max_length=60)
    code = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=30)