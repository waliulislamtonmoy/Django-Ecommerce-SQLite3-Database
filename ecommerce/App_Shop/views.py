from django.shortcuts import render


from .models import Category,Product


#authentication Mixin 
from django.contrib.auth.mixins import LoginRequiredMixin
#import views 
from django.views.generic import ListView,DetailView

# Create your views here.
class Home(ListView):
    model=Product
    template_name="App_Shop/home.html"
    

class Product_Detail(LoginRequiredMixin,DetailView):
    model=Product
    template_name="App_Shop/product_detail.html"
