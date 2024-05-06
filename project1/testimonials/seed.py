from django_seed import Seed 
from .models import Testimonials
import random

def runTestimonials():
    testimonials = ['Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam, risus at semper.','Export tempor illum tamen malis malis eram quae irure esse labore quem cillum quid cillum eram malis quorum velit fore eram velit sunt aliqua noster fugiat irure amet legam anim culpa.','Enim nisi quem export duis labore cillum quae magna enim sint quorum nulla quem veniam duis minim tempor labore quem eram duis noster aute amet eram fore quis sint minim.','Fugiat enim eram quae cillum dolore dolor amet nulla culpa multos export minim fugiat minim velit minim dolor enim duis veniam ipsum anim magna sunt elit fore quem dolore labore illum veniam.','Quis quorum aliqua sint quem legam fore sunt eram irure aliqua veniam tempor noster veniam enim culpa labore duis sunt culpa nulla illum cillum fugiat legam esse veniam culpa fore nisi cillum quid.']
    firstnames = ['Saul','Sara','Jena','Matt','John']
    names = ['Goodman','Wilsson','Karlis','Brandon','Larson']
    jobs = ['Ceo Founder','Designer','Store Owner','Freelancer','Entrepreneur']
    images = ['images/testimonials-1.jpg','images/testimonials-2.jpg','images/testimonials-3.jpg','images/testimonials-4.jpg','images/testimonials-5.jpg']

    for i in range(len(names)):
        Testimonials.objects.create(

        name = names[i],
        firstname = firstnames[i],
        testimonial = testimonials[i],
        job = jobs[i],
        image = images[i]
        )