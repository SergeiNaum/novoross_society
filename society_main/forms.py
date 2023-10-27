from django.forms import ModelForm
from django import forms
from django.forms import CheckboxInput

from society_main.models import ContactFormModel


class ContactForm(ModelForm):

    class Meta:
        model = ContactFormModel
        fields = ['name', 'email', 'message']
        labels = {'name': 'Ваше имя', 'email': 'Email', 'message': 'Сообщение'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-style', 'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-style', 'autocomplete': 'off'}),
            'message': forms.Textarea(attrs={
                'cols': 50, 'rows': 5, 'class': 'form-control form-style', 'autocomplete': 'off'
            }),
        }
