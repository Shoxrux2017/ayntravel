from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Offer)
class OfferTranslationOptions(TranslationOptions):
    fields =('title',) # text ckeditor

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields =('title', 'info')

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields =('info', 'address')

@register(Cat)
class CatTranslationOptions(TranslationOptions):
    fields = ('city','country')

@register(Operator)
class OperatorTranslationOptions(TranslationOptions):
    fields = ('author', 'post') # text ckeditor
