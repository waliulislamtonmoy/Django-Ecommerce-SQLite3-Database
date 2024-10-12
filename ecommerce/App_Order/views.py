from django.shortcuts import render

from django.shortcuts import render,get_object_or_404,redirect


#Authentications
from django.contrib.auth.decorators import login_required

#import model 
from App_Order.models import Cart,Order
from App_Shop.models import Product

# Create your views here.

@login_required
def add_to_cart(request,pk):
    item=get_object_or_404(Product,pk=pk)
    order_item=Cart.objects.get_or_create(item=item,user=request.user,purchase=False)
    order_qs=Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        if order.order_items.filter(item=item).exists():
            order_item[0].quantity +=1
            order_item.save()
            return redirect("App_Shop:home")
        else:
            order.order_items.add(order_item[0])
            return redirect("App_Shop:home")
    else:
        order=Order(user=request.user)
        order.save()
        order.order_items.add(order_item[0])
        return redirect("App_Shop:home")
            
            

