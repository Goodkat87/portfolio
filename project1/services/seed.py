from django_seed import Seed 
from .models import Services
import random

def runServices():
    tiltes = ['Lorem Ipsum','Dolor Sitema','Sed ut perspiciatis','Magni Dolores','Nemo Enim','Eiusmod Tempor']
    icons = ['briefcase','card-checklist','bar-chart','binoculars','brightness-high','calendar4-week']
    descriptions = ['Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident','Minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat tarad limino ata','Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur','Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum','At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque','Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi']

    for i in range(len(tiltes)):
        Services.objects.create(
            title = tiltes[i],
            icon = icons[i],
            description = descriptions[i]
        )