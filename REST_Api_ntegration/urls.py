
from django.contrib import admin
from django.urls import path,include
from contact_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('contact_app.urls')),
]