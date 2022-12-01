from django.urls import path
from rest_framework.authtoken import views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trainers', views.selectTrainerView, name="selectTrainerView"),
    path('api-token-auth/', views.obtain_auth_token)
]
