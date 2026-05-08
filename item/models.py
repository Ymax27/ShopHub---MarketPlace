from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['name',]
        verbose_name_plural = 'Categories'  #Defini manuellement le pluriel de Category dans l'admin dashboard
        
        
class Item(models.Model):
    
    def __str__(self):
        return self.name
    
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_solded = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)