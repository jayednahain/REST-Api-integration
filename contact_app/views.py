from django.http import JsonResponse
from django.shortcuts import render
from contact_app.models import ContactList
from .serializers import ContactListSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET','POST'])
def contact_list(request):
   #using get for retrive all the contact list data
   if request.method == 'GET':
      contact_list = ContactList.objects.all()

      #creating contact_list_serializer class instance
      serializer = ContactListSerializer(contact_list,many=True)

      return Response(serializer.data)

   elif request.method == 'POST':
      #de-serialize the data
      de_serializer = ContactListSerializer(data=request.data)

      if de_serializer.is_valid():
         de_serializer.save()
         return Response(de_serializer.data,status=status.HTTP_201_CREATED)
      return Response(de_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


api_view(['GET','PUT','DELETE'])
def contact_detail(request,pk):
   try:
      contact = ContactList.objects.get(pk=pk)
   except contact.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)


   if request.method =='GET':
      serializer = ContactListSerializer(contact)
      return Response(serializer.data)

   elif request.method == 'PUT':
      serializer = ContactListSerializer(contact,data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

   elif request.method =='DELETE':
      contact.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)


