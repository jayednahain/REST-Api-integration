
from django.urls import path,include
from contact_app import views

urlpatterns = [

    path('emp/',views.test_view),
]
