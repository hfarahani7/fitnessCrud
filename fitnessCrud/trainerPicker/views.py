from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("trainerPicker")

def selectTrainerView(request, trainer_list):
    return HttpResponse("selectTrainerView")

# def trainerView(request, trainer_id):

# Create your views here.
