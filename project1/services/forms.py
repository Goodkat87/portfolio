from django import forms
from .models import Services


class ServicesForm(forms.ModelForm):
  class Meta:
    model = Services
    fields = ['title','icon','description']
    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title'}),
        'icon': forms.Select(attrs={'class': 'form-select', 'placeholder': 'select an icon'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a brief description...'}),
    }