from django.db import models
class User(models.Model):
       id  =  models.AutoField(auto_created=True , primary_key=True)
       nom = models.CharField(max_length=200)
       prenom = models.CharField(max_length=200)
       profession = models.CharField(max_length=200)
       secteur = models.CharField(max_length=200)

       def __str__(self):
              return self.name