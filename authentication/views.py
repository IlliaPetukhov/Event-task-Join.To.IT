from .serializers import LoginEmailTokenObtainPairSerializer, RegistrationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LoginView(TokenObtainPairView):
    serializer_class = LoginEmailTokenObtainPairSerializer

class RegistrationView(APIView):
    def get_serializer(self, *args, **kwargs):
        return RegistrationSerializer(*args, **kwargs)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
