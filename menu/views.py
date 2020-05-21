from django.shortcuts import render
from .models import Menu
# Create your views here.
 
 
def menu_list(request):
    menu = Menu.objects.all()
    
    context ={
        'menu' : menu,
    }
    return render(request, 'Menu/menu.html', context)
