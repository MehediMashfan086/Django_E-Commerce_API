from django.urls import path
from api import views
urlpatterns = [
    path('categories/', views.ListCategory.as_view(), name= 'category'),
    path('categories/<int:pk>', views.DetailCategory.as_view(), name= 'singlecategory'),
    
    path('books/', views.ListBook.as_view(), name= 'book'),
    path('books/<int:pk>', views.DetailBook.as_view(), name= 'singlebook'),
    
    path('products/', views.ListProduct.as_view(), name= 'product'),
    path('products/<int:pk>', views.DetailProduct.as_view(), name= 'singleproduct'),
    
    path('users/', views.ListUser.as_view(), name= 'user'),
    path('users/<int:pk>', views.DetailUser.as_view(), name= 'singleuser'),
]
