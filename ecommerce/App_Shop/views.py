from django.shortcuts import render


from .models import Category,Product

#import views 
from django.views.generic import ListView,DetailView

# Create your views here.
class Home(ListView):
    model=Product
    template_name="App_Shop/home.html"
