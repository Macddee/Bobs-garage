from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField(max_length=1000)
    category = models.CharField(default="Uncategorized", max_length=50)
    
    def __str__(self):
        return self.title
    
    
