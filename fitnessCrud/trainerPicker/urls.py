from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trainers', views.selectTrainerView, name="selectTrainerView"),
]
