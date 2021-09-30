
from django.urls import path,include
from contact_app import views

urlpatterns = [

    path('contact_list/',views.contact_list),
    path('contact_detail/<int:pk>',views.contact_detail)



]
