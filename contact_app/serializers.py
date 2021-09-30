from rest_framework import serializers
from contact_app.models import ContactList



class ContactListSerializer(serializers.ModelSerializer):
   class Meta:
      model = ContactList
      fields = ['id','name','numbers']
