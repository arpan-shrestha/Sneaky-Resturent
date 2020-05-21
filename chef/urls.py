from django.urls import path
from . import views

app_name = 'chef'

urlpatterns = [
    path('',views.chef, name='chef'), 
]
