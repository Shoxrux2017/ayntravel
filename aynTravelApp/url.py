from django.urls import path,include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category),
    path('alltourpackages', alltourpackages, name='tourpackages'),
    path('about', aboutUs,name = 'about'),
    path('contact', contact, name='contact'),
    path('bronform', bronform, name='bronform'),
    path('contactform', contactForm, name='contactForm'),
]