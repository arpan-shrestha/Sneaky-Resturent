from django.shortcuts import render
from .models import AboutUs
from menu.models import Menu
# Create your views here.
def aboutus(request):
    about = AboutUs.objects.last()
    menu = Menu.objects.all()
 

    context={
        'about' : about,
        'menu' : menu,

    }
    return render(request, 'aboutus/about.html', context)
