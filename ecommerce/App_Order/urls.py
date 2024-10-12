from django.urls import path,include

app_name="App_Order"

from App_Order import views

urlpatterns = [
    path("add/<pk>/",views.add_to_cart,name="add")
]
