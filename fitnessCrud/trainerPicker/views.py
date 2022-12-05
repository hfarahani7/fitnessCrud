from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User

from requests import Response

from .models import GroupClass, Session
from .serializers import UserSerializer

def index(request):
    # return HttpResponse("trainerPicker")
    pass

def classSelector(request):
    pass

def trainerSelector(request):
    pass

def viewSchedule():
    # queries Session entries, returns rows matching by trainer, trainee, datetime range, or  
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


#q = GroupClass.objects.filter()
