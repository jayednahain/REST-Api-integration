
from django.urls import path,include
from contact_app import views

urlpatterns = [

    path('contact_list/',views.contact_list,name = 'contact_list_link'),
    path('contact_list/<str:name>',views.contact_detail,name='contact_detail_link')

]
