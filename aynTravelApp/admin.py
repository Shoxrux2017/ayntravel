from django import forms
from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# from ckeditor_uploader.widgets import CKEditorUploadingWidget

admin.site.register(ContactForm)


# class OfferAdminForm(forms.Modelorm):
#     text_uz = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
#     text_ru = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
#     text_en = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

#     class Meta:
#         model = Offer
#         fields = '__all__'

# class OperatorAdminForm(forms.Modelorm):
#     text_uz = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
#     text_ru = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
#     text_en = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

#     class Meta:
#         model = Operator
#         fields = '__all__'

@admin.register(Offer)
class OfferAdmin(TranslationAdmin):
    list_display = ('title',)


@admin.register(Contact)
class ContactAdmin(TranslationAdmin):
    list_display = ('info', 'address')


@admin.register(Cat)
class CatAdmin(TranslationAdmin):
    list_display = ('city', 'country')


@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ('title',)

@admin.register(Operator)
class OperatorAdmin(TranslationAdmin):
    list_display = ('author', 'post')


