from django.urls import path

app_name='App_Account'

from App_Account import views

urlpatterns = [
    path("signup/",views.signup,name='signup'),
    path("login/",views.userlogin,name='login'),
    path("logout/",views.user_logout,name="logout")
]