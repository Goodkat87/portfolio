import django
django.setup()
from about.seed import runAbout
from skills.seed import runSkills
from portfolio.seed import runPortfolio
from services.seed import runServices
from testimonials.seed import runTestimonials
from contact.seed import runContact

# if __name__ == "__main__":
#     runAbout()

# if __name__ == "__main__":
#     runSkills()

# if __name__ == "__main__":
#     runPortfolio()


# if __name__ == "__main__":
#      runServices()

if __name__ == "__main__":
     runTestimonials()

# if __name__ == "__main__":
#      runContact()


