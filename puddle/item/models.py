from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey("Category", verbose_name='Category', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to="item_images")
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, verbose_name='created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=False)
    def __str__(self):
        return self.name


    
