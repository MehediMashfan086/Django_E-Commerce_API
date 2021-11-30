from django.urls import path
from api import views
urlpatterns = [
    path('categories/', views.ListCategory.as_view()),
    path('categories/<int:pk>', views.DetailCategory.as_view()),
    
    path('books/', views.ListBook.as_view()),
    path('books/<int:pk>', views.DetailBook.as_view()),
    
    path('products/', views.ListProduct.as_view()),
    path('products/<int:pk>', views.DetailProduct.as_view()),
]
