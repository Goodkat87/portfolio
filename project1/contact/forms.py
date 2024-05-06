from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = ['description','street','number','locality','code','email','phone']