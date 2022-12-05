from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import permissions

from requests import Response

from .models import TrainerData
from .serializers import UserSerializer, TrainerDataSerializer

def index(request):
    # return HttpResponse("trainerPicker")
    pass

def create_user(ModelViewSet):
    serializer_class = UserSerializer
    query_set = User.objects.all()
  
    def perform_create(self, serializer):
        password = self.request.data['password']
        password2 = self.request.data['password2']
        if (password==password2):
            serializer.save()
            return Response('User was created')
        else:
            return Response('Password did not match')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class TrainerDataViewSet(viewsets.ModelViewSet):
    queryset = TrainerData.objects.all()
    serializer_class = TrainerDataSerializer
    permission_classes = [permissions.IsAuthenticated]

#q = GroupClass.objects.filter()
