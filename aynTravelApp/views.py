from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm,OfferForm
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q 
from django.views.generic import ListView
def index(request):
    services = Services.objects.all()
    category = Cat.objects.all()
    lastoffers = Offer.objects.all().order_by('created_at')[:2]
    offers = Offer.objects.all() 
    aboutUs = About.objects.all()
    context = { 
        'lastoffers' : lastoffers,
        'offers' : offers,
        'category':category,
        'services': services,
        'abouts' : aboutUs,
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
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            context = {'success':1}

    else:
        form = ContactForm()
    context = {
        'form':form
    }
    return render(request, 'aynTravelApp/contact.html',context = context)
              

def handle_uploaded_file(f):
    with open('Photos/%Y/%m/%d'+ f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)            


def bronform(request): 
    if request.method == "POST":
        form = OfferForm(request.POST,request.FILES) 
        if form.is_valid():
            # form.save()
            # return redirect('home')
            handle_uploaded_file(request.FILES['file'])
            offer = Offer.objects.create(**form.cleaned_data)
            return redirect(offer)
    else:
        form = OfferForm()
    return render(request, 'aynTravelApp/offerform.html',{'form' : form})
    

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
    search_query = request.GET.get('search', '')
    if search_query:
        offer = Offer.objects.filter(Q(title__icontains = search_query) | Q(info__icontains = search_query) | Q(price__icontains = search_query))
    else:
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

