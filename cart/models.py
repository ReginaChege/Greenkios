from django.db import models
from inventory.models import Product

class Cart(models.Model):
    products = models.ManyToManyField(Product)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    shippingcost = models.DecimalField(max_digits=6, decimal_places=2)
    paymentoptions = models.CharField(max_length=15)

    def add_product(self, product):
        self.products.add(product)
        self.save()
        return self
    def get_total_price(self):
        products=self.products
        total=0
        for product in products:
            total += product.price
        return total

    def __str__(self):
        return f"Cart {self.pk}"