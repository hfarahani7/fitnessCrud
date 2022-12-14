"""fitnessCrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.contrib.auth.models import User
from rest_framework import routers

from trainerPicker import views as v
from trainerPicker import api

from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.register(r'users', v.UserViewSet)
router.register(r'trainers', v.TrainerDataViewSet)
router.register(r'trainees', v.TraineeDataViewSet)
router.register(r'groupclass', v.GroupClassViewSet)
router.register(r'session', v.SessionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
    path('create-user/', api.CreateUserView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls))
]
