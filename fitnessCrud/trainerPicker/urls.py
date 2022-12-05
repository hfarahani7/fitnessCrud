from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from . import views as v

router = routers.DefaultRouter()
router.register(r'trainers', v.TrainerDataViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('create-user', views.create_user.as_view())
]
