
from .models import User,Profile
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm

#UserProfileCreationForm

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields="__all__"
        exlude=('user')
        
class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['email','password1','password2']
        

