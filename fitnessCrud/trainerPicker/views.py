from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Trainer

def index(request):
    return HttpResponse("trainerPicker")

def selectTrainerView(request, trainer_list):
    return HttpResponse("selectTrainerView")

# def trainerView(request, trainer_id):

# Create your views here.
