from django_seed import Seed 
from .models import Contact
import random

entries = [
    {
        'description':'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
        'street':'Adam Street',
        'number':'108',
        'locality':'New York',
        'code':'535022',
        'email':'info@example.com',
        'phone':'+1 5589 55488 55s'
    }
    ]

def runContact():
    seeder = Seed.seeder()
    for i in entries:
        seeder.add_entity(Contact,1,{
            'description': i['description'],
            'street': i['street'],
            'number': i['number'],
            'locality': i['locality'],
            'code': i['code'],
            'phone': i['phone'],
            'email': i['email'],
        })
    pks = seeder.execute()
    print(pks)