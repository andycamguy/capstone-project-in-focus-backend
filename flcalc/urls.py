from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UserCameraSettingsView
router = DefaultRouter()
router.register(r'fstop', views.FStopViewSet)
router.register(r'lens', views.LensViewSet)
router.register(r'cameramodel', views.CameraModelViewSet)
router.register(r'modelfstop', views.ModelFStopViewSet)
router.register(r'modellens', views.ModelLensViewSet)
router.register(r'dslrcamera', views.DSLRCameraViewSet)
router.register(r'iso', views.ISOViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'usercamerasettings', views.UserCameraSettingsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
     path('user-settings/', UserCameraSettingsView.as_view(), name='user-camera-settings'),
]
