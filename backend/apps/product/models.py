from django.db import models
from apps.store.models import Store
  

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.TextField(verbose_name="Description")
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    quantity_in_stock = models.IntegerField(verbose_name="Quantity in Stock")
    availability_status = models.BooleanField(default=True, verbose_name="Availability Status")
    categories = models.ManyToManyField(Category, related_name='products')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
    

  