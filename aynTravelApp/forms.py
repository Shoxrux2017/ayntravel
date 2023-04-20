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

class OfferForm(forms.Form):
    title = forms.CharField(
        max_length=150, 
        label=' заголовок ', 
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
            )
        )
    info = forms.CharField(max_length=400, 
        label=' текст ', 
        widget=forms.Textarea(
            attrs={'class': 'form-control','rows':5}
            )
        )
    price = forms.CharField(
        max_length=150, 
        label=' цена ', 
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}
            )
        )
    category = forms.ModelChoiceField(
        empty_label=' выберите категорию ',
        queryset=Cat.objects.all(), 
        widget=forms.Select(
            attrs={'class': 'form-control'}
            )
        )
    is_published = forms.BooleanField( 
        label=' опубликовано ',
        initial=True)
    photo = forms.FileField()

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='name',
        widget= forms.TextInput(
            attrs={"name":"field1", "class": "field-divided"}
        )
    )
    email = forms.EmailField(
        label='email',
        widget= forms.TextInput(
            attrs={"name":"field3", "class": "field-long"}
        )
    )
    message = forms.CharField(
        min_length=10,
        label='message',
        widget=forms.Textarea(
            attrs={"id":"field5","name":"field5",'class':'field-long field-textare'}
        )
    ) 



