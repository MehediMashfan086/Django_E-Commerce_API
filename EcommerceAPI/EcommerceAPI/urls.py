from django.contrib import admin
from django.urls import include, path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
]
