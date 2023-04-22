from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q 
from django.views.generic import ListView
def index(request):
    category = Cat.objects.all()
    lastoffers = Offer.objects.all().order_by('created_at')[:2]
    offers = Offer.objects.all() 
    aboutUs = About.objects.all()
    operator = Operator.objects.all()
    context = { 
        'lastoffers' : lastoffers,
        'offers' : offers,
        'categories':category,
        'abouts' : aboutUs,
        'operator' : operator,
    }
    return render(request, template_name='aynTravelApp/index.html',context=context)

def contact(request):
    category = Cat.objects.all()
    contactDetails = Contact.objects.all()
    context = {
        'contacts':contactDetails,
        'category':category,
    }
    return render(request, 'aynTravelApp/contact.html',context=context)

def aboutUs(request):
    aboutUs = About.objects.all()
    context = {
        'abouts' : aboutUs,
    }
    return render(request, 'aynTravelApp/about.html',context=context)
    
def contactForm(request):
    if request.method == 'POST':
        
        message_message = request.POST['message-message']
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        
        # contact = ContactForm()

        # message = request.POST.get('message')
        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # subject = request.POST.get('subject')

        # contact.message = message
        # contact.name = name
        # contact.email = email
        # contact.subject = subject
        # contact.save()
        # return HttpResponse('<h1>Thanks for message!</h1>')
        return render(request, 'aynTravelApp/contact.html', {'message_message':message_message, 'message_name':message_name})

    else:
        return render(request, 'aynTravelApp/contact.html')
              

def handle_uploaded_file(f):
    with open('Photos/%Y/%m/%d'+ f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)            


def bronform(request, category_id): 
    offer = Offer.objects.filter(category_id=category_id)
    categories = Cat.objects.all()
    category = Cat.objects.filter(pk=category_id)
    context = {'offers':offer,
                'categories': categories,
                'category':category      
    }

    return render(request, 'aynTravelApp/blog.html')

def view_offer(request, offer_id):
    category = Cat.objects.all()
    offer = get_object_or_404(Offer, pk=offer_id)
    return render(request, 'aynTravelApp/view_offer.html', {"offer" : offer, "categories": category})
    

def get_category(request, category_id):
    offer = Offer.objects.filter(category_id=category_id)
    categories = Cat.objects.all()
    category = Cat.objects.filter(pk=category_id)
    context = {'offers':offer,
                'categories': categories,
                'category':category
            
    }
    return render(request, 'aynTravelApp/hotel.html',context=context)



def alltourpackages(request):
    offer = Offer.objects.all()
    category = Cat.objects.all()
    context = {'offers':offer,
                'categories':category,
    }
    return render(request, 'aynTravelApp/hotel.html',context=context)  

# def send_message(name, email, message):
#     text = get_template('aynTravelApp/message.html')
#     html = get_template('aynTravelApp/message.html')
#     context = {'name':name,'email':email,'message':message}
#     subject = 'Сообщение от пользователя'
#     from_email = 'from@example.com'
#     text_content = text.render(context)
#     html_content = text.render(context)

#     msg = EmailMultiAlternatives(subject,text_content,from_email,['manager@example.com'])
#     msg.attach_alternative(html_content, text/html)
#     msg.send()

