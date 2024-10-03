from django.urls import path,include

app_name='App_Shop'
from App_Shop import views

urlpatterns = [
    path("",views.Home.as_view(),name="home")
]