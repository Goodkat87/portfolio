from django import forms
from .models import Infos


class InfosForm(forms.ModelForm):
  class Meta:
    model = Infos
    fields = ['title','subtitle','birthday','website','phone','city','age','degree','email','disponibility','details','description','picture']
    widget={
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
      'birthday': forms.TextInput(attrs={'class': 'form-control'}),
      'website': forms.TextInput(attrs={'class': 'form-control'}),
      'phone': forms.TextInput(attrs={'class': 'form-control'}),
      'city': forms.TextInput(attrs={'class': 'form-control'}),
      'degree': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.TextInput(attrs={'class': 'form-control'}),
      'disponibility': forms.Select(attrs={'class': 'form-select'}),
      'details': forms.Textarea(attrs={'class':'form-control'}),
      'description': forms.Textarea(attrs={'class': 'form-control'}),
      'picture':forms.FileInput(attrs={'class':'form-control'}),
    }

    