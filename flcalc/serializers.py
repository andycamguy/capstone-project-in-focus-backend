from rest_framework import serializers
from .models import FStop, Lens, CameraModel, ModelFStop, ModelLens, DSLRCamera, ISO, User, UserCameraSettings

class FStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = FStop
        fields = '__all__'

class LensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lens
        fields = '__all__'

class CameraModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CameraModel
        fields = '__all__'

class ModelFStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelFStop
        fields = '__all__'

class ModelLensSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelLens
        fields = '__all__'

class DSLRCameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = DSLRCamera
        fields = '__all__'

class ISOSerializer(serializers.ModelSerializer):
    class Meta:
        model = ISO
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserCameraSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCameraSettings
        fields = '__all__'
