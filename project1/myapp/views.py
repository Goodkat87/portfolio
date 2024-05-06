from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse

# Create your views here.
from about.models import Infos
from skills.models import Skills
from portfolio.models import Portfolio
from services.models import Services
from testimonials.models import Testimonials
from contact.models import Contact
from about.forms import InfosForm
from testimonials.forms import TestimonialForm
from services.forms import ServicesForm
from portfolio.forms import PortfolioForm
from skills.forms import SkillsForm
from contact.forms import ContactForm


def home(request):
    infos = Infos.objects.first()
    contact = Contact.objects.first()
    skills = Skills.objects.all()
    portfolios = Portfolio.objects.all()
    services = Services.objects.all()
    testimonials = Testimonials.objects.all()
    return render(request, "index.html",{"infos":infos,"skills":skills,'portfolios':portfolios,'services':services,'testimonials':testimonials,'contact':contact})

def back(request):

    infos = Infos.objects.first()
    contact = Contact.objects.first()
    skills = Skills.objects.all()
    portfolios = Portfolio.objects.all()
    services = Services.objects.all()
    testimonials = Testimonials.objects.all()


    return render(request, "back.html",{"infos":infos,"skills":skills,'portfolios':portfolios,'services':services,'testimonials':testimonials,'contact':contact})

#TESTIMONIALS
def delete_testimonials(request,id):
    testimonial = Testimonials.objects.get(id=id)
    testimonial.delete()
    return redirect("back")

def add_testimonials(request):
    if request.method == "POST":
        form =  TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('back')
    else:
        form = TestimonialForm()
    return render(request,'add_testimonials.html',{'form':form})

#SERVICES

def delete_services(request,id):
    services = Services.objects.get(id=id)
    services.delete()
    return redirect("back")

def add_services(request):
    if request.method == "POST":
        form =  ServicesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('back')
    else:
        form = ServicesForm()
    return render(request,'add_services.html',{'form':form})

#PORTFOLIO

def delete_portfolio(request,id):
    portfolio = Portfolio.objects.get(id=id)
    portfolio.delete()
    return redirect("back")

def add_portfolio(request):
    if request.method == "POST":
        form =  PortfolioForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('back')
    else:
        form = PortfolioForm()
    return render(request,'add_portfolio.html',{'form':form})

#SKILLS
def delete_skills(request,id):
    skills = Skills.objects.get(id=id)
    skills.delete()
    return redirect("back")

def add_skills(request):
    if request.method == "POST":
        form = SkillsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('back')
    else:
        form = SkillsForm()
    return render(request,'add_skills.html',{'form':form})

#ABOUT
def update_about(request, id):
    about = Infos.objects.get(id=id)
    form = InfosForm(request.POST or None, request.FILES, instance=about)
    if form.is_valid():
        form.save()
        return redirect('back')
    else:
        form = InfosForm(instance=about)
    return render(request, 'update_about.html', {'form':form})


#CONTACT

def update_contact(request, id):
    contact = Contact.objects.get(id=id)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('back')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'update_contact.html', {'form':form})