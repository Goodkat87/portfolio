from django_seed import Seed 
from .models import Portfolio
import random

def runPortfolio():
    names=['App 1','Web 3','App 2','Card 2','Web 2','App 3','Card 1','Card 3','Web 3']
    categories = ['app','web','app','card','web','app','card','card','web']
    images = ['images/portfolio-1.jpg','images/portfolio-2.jpg','images/portfolio-3.jpg','images/portfolio-4.jpg','images/portfolio-5.jpg','images/portfolio-6.jpg','images/portfolio-7.jpg','images/portfolio-8.jpg','images/portfolio-9.jpg']



    for i in range(len(names)):
        Portfolio.objects.create(
            name = names[i],
            categorie = categories[i],
            description = '',
            image = images[i]
        )