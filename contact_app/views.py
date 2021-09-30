from django.http import JsonResponse
from django.shortcuts import render
JsonResponse


# Create your views here.


def test_view(request):

   contact_data = {
      'name':'jayed nahian',
      'number':'1233245'
   }


   return JsonResponse(contact_data) #serialize the dictionary data as Jsonresponse