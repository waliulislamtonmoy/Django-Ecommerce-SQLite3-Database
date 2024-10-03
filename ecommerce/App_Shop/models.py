from django.db import models



# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.title)
    class Meta :
        verbose_name_plural="Categories"
        
class Product(models.Model):
    mainimage=models.ImageField(upload_to="products/",blank=True)
    name=models.CharField( max_length=250) 
    category=models.ForeignKey(Category, on_delete=models.CASCADE,related_name="category")
    preview_text=models.TextField(max_length="140",verbose_name="preview_text")
    detail_text=models.TextField(max_length="1000",verbose_name="detail_text")
    price=models.FloatField()
    old_price=models.FloatField(default=0.00)
    created=models.DateTimeField( auto_now_add=True)
    
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering=['-created',]