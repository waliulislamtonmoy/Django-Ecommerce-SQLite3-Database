from django.urls import path,include

app_name='App_Shop'
from App_Shop import views

urlpatterns = [
    path("",views.Home.as_view(),name="home"),
    path("product_detail/<pk>/",views.Product_Detail.as_view(),name="product_detail"),
]