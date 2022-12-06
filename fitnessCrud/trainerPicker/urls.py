from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from . import views as v
from . import api

urlpatterns = [
    path('', views.index, name='index'),
    path('api-token-auth/', views.obtain_auth_token),
    path('create-user/', api.CreateUserView)
]
