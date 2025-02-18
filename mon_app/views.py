from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

from .serializer import UserSerializer

from .models import User

from rest_framework import generics

class UserListView(generics.ListCreateAPIView):
       queryset = User.objects.all()
       serializer_class = UserSerializer

class UserCreateView(generics.CreateAPIView):
       queryset = User.objects.all()
       serializer_class = UserSerializer

class UserRetrieveView(generics.RetrieveAPIView):
       queryset = User.objects.all()
       serializer_class = UserSerializer
       lookup_field = 'id'

class UserUpdateView(generics.RetrieveUpdateAPIView):
       queryset = User.objects.all()
       serializer_class = UserSerializer

class UserDelateView(generics.RetrieveDestroyAPIView):
       queryset = User.objects.all()
       serializer_class = UserSerializer