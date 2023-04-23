from django.urls import path,include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name="get_category"),
    path('alltourpackages', alltourpackages, name='offer'),
    path('offer/<int:offer_id>/', view_offer, name='view_offer'),
    path('about', aboutUs,name = 'about'),
    path('bronform', bronform, name='bronform'),
    path('contactForm', contactForm, name='contactForm'),
]