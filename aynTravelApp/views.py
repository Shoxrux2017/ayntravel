from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, send_mail
from django.db.models import Q 
from django.views.generic import ListView
from .forms import ContactForm


def index(request):
    category = Cat.objects.all()
    lastoffers = Offer.objects.all().order_by('created_at')[:2]
    offers = Offer.objects.all() 
    aboutUs = About.objects.all()
    operator = Operator.objects.all()
    contacts = Contact.objects.all()
    context = { 
        'lastoffers' : lastoffers,
        'offers' : offers,
        'categories':category,
        'abouts' : aboutUs,
        'operator' : operator,
        'contacts': contacts,
    }
    return render(request, template_name='aynTravelApp/index.html',context=context)



def aboutUs(request):
    aboutUs = About.objects.all()
    category = Cat.objects.all()
    contacts = Contact.objects.all()
    context = {
        'abouts' : aboutUs,
        'categories':category,
        'contacts': contacts,
    }
    return render(request, 'aynTravelApp/about.html',context=context)
    
def contactForm(request):
    category = Cat.objects.all()
    contacts = Contact.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            
            html= render_to_string('aynTravelApp/emails/email.html', {
                'message':message,
                'name' : name,
                'email':email,
                'subject':subject,
            })
            send_mail('The contact form subject', 'This is the message', 'akobirovazimkhon@gmail.com',['shootnick001@gmail.com'], html_message=html)
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'aynTravelApp/contact.html', {'form': form, 'categories':category,'contacts': contacts})



def handle_uploaded_file(f):
    with open('Photos/%Y/%m/%d'+ f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)            


def view_offer(request, offer_id):
    contacts = Contact.objects.all()
    category = Cat.objects.all()
    offer = get_object_or_404(Offer, pk=offer_id)
    return render(request, 'aynTravelApp/view_offer.html', {"offer" : offer, "categories": category,'contacts': contacts})
    

def get_category(request, category_id):
    contacts = Contact.objects.all()
    offer = Offer.objects.filter(category_id=category_id)
    categories = Cat.objects.all()
    category = Cat.objects.filter(pk=category_id)
    context = {'offers':offer,
                'categories': categories,
                'category':category,
                'contacts': contacts
            
    }
    return render(request, 'aynTravelApp/hotel.html',context=context)



def alltourpackages(request):
    contacts = Contact.objects.all()
    offer = Offer.objects.all()
    category = Cat.objects.all()
    context = {'offers':offer,
                'categories':category,
                'contacts': contacts
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

