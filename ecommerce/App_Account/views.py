from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse

#Authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

#Forms And Models
from .models import User,Profile
from .forms import ProfileForm,SignUpForm


# Create your views here.

def signup(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect(reverse('App_Account:login'))
    return render(request,'App_Account/signup.html',{'form':form})

def userlogin(request):
    form=AuthenticationForm()
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponse("Congratulations Welcome to Django | E-com")
    return render(request,"App_Account/login.html",{'form':form})

@login_required
def user_logout(request):
    logout(request)
    
    return render(request,"App_Account/login.html")

@login_required
def user_profile(request):
    profile=Profile.objects.get(user=request.user)
    form=ProfileForm(instance=profile)
    if request.method=="POST":
        form=ProfileForm(data=request.POST,instance=profile)
        if form.is_valid():
            form.save()
           
            form=ProfileForm(instance=profile)
    return render(request,'App_Account/change_profile.html',{'form':form})
        

