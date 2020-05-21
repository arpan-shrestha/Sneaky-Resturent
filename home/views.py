from django.shortcuts import render
from menu.models import Menu
from aboutus.models import AboutUs
from .models import Offer
from chef.models import Chef
from contact.forms import contactForm
# Create your views here.
def home(request):
    chef = Chef.objects.all()
    offer = Offer.objects.last()
    menu = Menu.objects.all()
    about = AboutUs.objects.last()


    context ={
        'chef':chef,
        'offer':offer,
        'menu':menu,
        'about':about,
    }
    return render (request, 'home/index.html', context)



