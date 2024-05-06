from django.db import models

# Create your models here.

class Services(models.Model):
    ICON_CHOICES=(
        ("briefcase","briefcase"),
        ("card-checklist","checklist"),
        ("bar-chart","bar-chart"),
        ("binoculars","binoculars"),
        ("brightness-high","brightness-high"),
        ("calendar4-week","calendar4-week"),
    )
    title = models.CharField(max_length=40)
    icon = models.CharField(max_length=30, choices=ICON_CHOICES)
    description = models.CharField(max_length=200)