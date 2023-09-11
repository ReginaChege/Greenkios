from django.db import models

# Create your models here.
class MamaMboga(models.Model):
    name = models.CharField(max_length=30)
    location=models.TextField()
    contact=models.IntegerField()
    password=models.CharField(max_length=8)
    storename=models.CharField(max_length=8)
    username=models.CharField(max_length=8)
    def __str__(self):
        return self.name