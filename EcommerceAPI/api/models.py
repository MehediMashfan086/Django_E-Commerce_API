from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=260)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name = 'books',
                                 on_delete = models.CASCADE)
    author = models.CharField(max_length=100, default='Mehedi Hasan')
    isbn = models.CharField(max_length=15)
    pages = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    imageUrl = models.URLField()
    created_by = models.ForeignKey('auth.User', related_name = 'books',
                                 on_delete = models.CASCADE, null = True)
    status = models.BooleanField(default = True)
    date_created = models.DateField(auto_now_add= True)
    
    class Meta:
        ordering = ['-date_created']
        
    def __str__(self):
        return self.title

class Product(models.Model):
    product_tag = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name = 'products',
                        on_delete = models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageUrl = models.URLField()
    created_by = models.ForeignKey('auth.User', related_name = 'products',
                                 on_delete = models.CASCADE, null = True)
    status = models.BooleanField(default = True)
    date_created = models.DateField(auto_now_add= True)
    
    class Meta:
        ordering = ['-date_created']
        
    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)