from django.db import models


class ContactList(models.Model):
   id       = models.IntegerField(unique=True,primary_key=True)
   name     = models.CharField(max_length=100)
   numbers  = models.CharField(max_length=50,unique=True)

   def __str__(self):
      return self.name , ' ', self.numbers