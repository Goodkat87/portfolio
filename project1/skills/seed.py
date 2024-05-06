from django_seed import Seed 
from .models import Skills
import random




def runSkills():
    names = ['HTML','CSS ','JavaScript','PHP','WordPress/CMS','Photoshop']
    percents = [100,90,75,80,90,55,]
    for i in range(len(names)):
        Skills.objects.create(
            name = names[i],
            percent = percents[i]
        )