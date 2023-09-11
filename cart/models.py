from django.db import models
from inventory.models import Product

class Cart(models.Model):
    products = models.ManyToManyField(Product)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    shippingcost = models.DecimalField(max_digits=6, decimal_places=2)
    paymentoptions = models.CharField(max_length=15)

    def __str__(self):
        return f"Cart {self.pk}"