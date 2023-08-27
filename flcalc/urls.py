from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UserCameraSettingsView


urlpatterns = [

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
     path('user/', UserCameraSettingsView.as_view(), name='user-camera-settings'),
]
