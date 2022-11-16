from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("trainerPicker")

# Create your views here.
