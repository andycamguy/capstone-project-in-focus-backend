from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserCameraSettings
from .serializers import UserCameraSettingsSerializer

class UserCameraSettingsView(APIView):
    def get(self, request):
        user = request.user  # Assuming you're using authentication
        try:
            settings = UserCameraSettings.objects.get(user=user)
            serializer = UserCameraSettingsSerializer(settings)
            return Response(serializer.data)
        except UserCameraSettings.DoesNotExist:
            return Response(
                {"error": "User settings not found"},
                status=status.HTTP_404_NOT_FOUND
            )