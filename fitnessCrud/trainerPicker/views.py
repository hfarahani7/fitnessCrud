from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import GroupClass, Session

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
# Create your views here.

#q = GroupClass.objects.filter()
