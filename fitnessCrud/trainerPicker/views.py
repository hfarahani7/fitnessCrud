from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import permissions

from requests import Response

from .models import TrainerData, TraineeData, GroupClass, Session
from .serializers import UserSerializer, TrainerDataSerializer, TraineeDataSerializer, GroupClassSerializer, SessionSerializer

def index(request):
    # return HttpResponse("trainerPicker")
    pass

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class TrainerDataViewSet(viewsets.ModelViewSet):
    queryset = TrainerData.objects.all()
    serializer_class = TrainerDataSerializer
    permission_classes = [permissions.IsAuthenticated]

class TraineeDataViewSet(viewsets.ModelViewSet):
    queryset = TraineeData.objects.all()
    serializer_class = TraineeDataSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupClassViewSet(viewsets.ModelViewSet):
    queryset = GroupClass.objects.all()
    serializer_class = GroupClassSerializer
    permission_classes = [permissions.IsAuthenticated]

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [permissions.IsAuthenticated]
#q = GroupClass.objects.filter()
