from django.forms import ModelForm
from django import forms
from captcha.fields import CaptchaField

from society_main.models import ContactFormModel


class ContactForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = ContactFormModel
        fields = ['name', 'email', 'message', 'checkbox', 'captcha']
        labels = {
            'name': 'Ваше имя',
            'email': 'Email',
            'message': 'Сообщение',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-style', 'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-style', 'autocomplete': 'off'}),
            'message': forms.Textarea(attrs={
                'cols': 50, 'rows': 5, 'class': 'form-control form-style', 'autocomplete': 'off'
            }),
            'checkbox': forms.CheckboxInput(attrs={
                'class': 'chechbox_in', 'id': 'checkbox', 'required': True}),
        }
