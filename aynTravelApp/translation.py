from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Offer)
class OfferTranslationOptions(TranslationOptions):
    fields =('title', 'info')

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields =('info', 'address')

@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields =('title', 'info')

@register(Cat)
class CatTranslationOptions(TranslationOptions):
    fields = ('title',)
