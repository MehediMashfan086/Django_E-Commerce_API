from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 
                  'title'
        ]
    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 
                  'title',
                  'category',
                  'isbn',
                  'pages',
                  'price',
                  'stock',
                  'description',
                  'imageUrl',
                  'status',
                  'date_created'
                  
        ]
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 
                  'product_tag',
                  'name',
                  'category',
                  'price',
                  'stock',
                  'imageUrl',
                  'status',
                  'date_created'
                  
        ]

class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many = True, queryset = 
            Book.objects.all())
    products = serializers.PrimaryKeyRelatedField(many = True, queryset = 
            Product.objects.all())
    
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'books',
            'products'
        ]
        