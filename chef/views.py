from django.shortcuts import render
from .models import Chef

# Create your views here.
def chef(request):
    chef = Chef.objects.all()

    context={
        'chef' : chef,
    }
    return render(request, 'chef/chef.html', context)