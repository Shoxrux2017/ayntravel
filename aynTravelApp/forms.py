from django import forms
from .models import *
# class OfferForm(forms.ModelForm):
#     class Meta:
#         model = Offer 
#         fields = ["title", "info", "price", "is_published", "category",'photo']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'info': forms.Textarea(attrs={'class': 'form-control', 'rows':5}),
#             'price': forms.TextInput(attrs={'class': 'form-control'}),
#             'category': forms.Select(attrs={'class': 'form-control'}),
#             }

# class OfferForm(forms.ModelForm):
#     name = forms.CharField(
#         max_length=150, 
#         label=' заголовок ', 
#         widget=forms.TextInput())

#     email = forms.CharField(max_length=400, 
#         label=' текст ', 
#         widget=forms.EmailField())

#     phone = forms.CharField(
#         max_length=150, 
#         label= 'цена', 
#         widget=forms.NumberInput())

#     category = forms.ModelChoiceField(
#         empty_label=' выберите категорию ',
#         queryset=Cat.objects.all(), 
#         widget=forms.Select())



# class ContactForm(forms.Form):
#     name = forms.CharField(
#         max_length=100,
#         label='name',
#         widget= forms.TextInput(
#             attrs={"name":"field1", "class": "field-divided"}
#         )
#     )
#     email = forms.EmailField(
#         label='email',
#         widget= forms.TextInput(
#             attrs={"name":"field3", "class": "field-long"}
#         )
#     )
#     message = forms.CharField(
#         min_length=10,
#         label='message',
#         widget=forms.Textarea(
#             attrs={"id":"field5","name":"field5",'class':'field-long field-textare'}
#         )
#     ) 

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        # fields = '__all__'
        fields = ['message', 'name', 'email', 'subject']
        # widgets = {
        #     'message': forms.Textarea(attrs={'class': 'form-control w-100', 'cols':30, 'rows':9, 'placeholder': 'Enter Message'}),
        #     'name': forms.TextInput(attrs={'class': 'form-control valid', 'placeholder': 'Enter your name', "id":"name","name":"message-name", }),
        #     'email': forms.EmailField(attrs={'class': 'form-control valid', 'placeholder': 'Enter email address', "id":"email","name":"message-email",}),
        #     'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subject', "id":"subject","name":"message-subject",}),
        # }




