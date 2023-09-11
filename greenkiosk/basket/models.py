from django.db import models

# Create your models here.
class Basket(models.Model):
     basket_name=models.CharField(max_length=30)
     basket_number=models.IntegerField()
     items_baskets=models.CharField(max_length=500)
     created_at=models.DateTimeField(auto_now_add=True)
     updated_at=models.DateTimeField(auto_now=True)
def __str__(self):
    return self.basket_name
