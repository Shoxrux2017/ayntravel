from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'
        # fields = ['message', 'name', 'email', 'subject']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control w-100', 'cols':30, 'rows':9, 'placeholder': 'Enter Message'}),
            'name': forms.TextInput(attrs={'class': 'form-control valid', 'placeholder': 'Enter your name', "id":"name","name":"message-name", }),
            'email': forms.EmailInput(attrs={'class': 'form-control valid', 'placeholder': 'Enter email address', "id":"email","name":"message-email",}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subject', "id":"subject","name":"message-subject",}),
        }




