from django.db import models

from App_Shop.models import Product
# Create your models here.
from django.conf import settings

class Cart(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE,related_name='cart')
    item=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    purchase = models.BooleanField(default=False)
    created=models.DateTimeField( auto_now_add=True)
    updated_cart=models.DateTimeField( auto_now=True, )
    
    def __str__(self):
        return f'{self.quantity} X {self.item}'
    def get_total(self):
        total=self.item.price * self.quantity
        float_total=format(total,'0.2f')
        return float_total
    
class Order(models.Model):
    order_items=models.ManyToManyField(Cart)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='oreder_list')
    ordered=models.BooleanField(default=False)
    created=models.DateTimeField( auto_now_add=True)
    payment_id=models.CharField(max_length=256,blank=True,null=True)
    order_id=models.CharField(max_length=256,blank=True,null=True)
    
    
    def get_total(self):
        total=0
        for order_item in self.order_items.all():
            total +=float(order_item.get_total())
        return total
    