from django.forms import ModelForm

from society_main.models import ContactFormModel


class ContactForm(ModelForm):
    class Meta:
        model = ContactFormModel
        fields = ['name', 'email', 'message']
