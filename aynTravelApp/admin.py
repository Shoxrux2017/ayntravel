from django.contrib import admin
from .models import *
# from modeltranslation.admin import TranslationAdmin

admin.site.register(Offer)
admin.site.register(Contact)
admin.site.register(Services)
admin.site.register(Cat)
admin.site.register(About)
# @admin.register(Offer)
# class OfferAdmin(TranslationAdmin):
#     list_display = ('title','info')

# @admin.register(Contact)
# class ContactAdmin(TranslationAdmin):
#     list_display = ('info','address')

# @admin.register(Services)
# class ServicesAdmin(TranslationAdmin):
#     list_display = ('title','info')

# @admin.register(Cat)
# class CatAdmin(TranslationAdmin):
#     list_display = ('title',)
