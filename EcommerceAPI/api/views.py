from django.shortcuts import render
from rest_framework import generics
from .serializers import *

# Create your views here.
class ListCategory(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
