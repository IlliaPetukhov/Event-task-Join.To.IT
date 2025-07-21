from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from Event.permissions import ReadOnly
from .models import User
from .serializers import UserSerializerGet, UserSerializerPost, OrganizerSerializerGet, EmailTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class LoginView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer



class UserViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
    
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return UserSerializerGet
        return UserSerializerPost
    
    def get_permissions(self):
        if self.action == "create":
            return [AllowAny(),]
        return [IsAuthenticated()]
    
class OrganizerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.prefetch_related("organizer").all()
    serializer_class = OrganizerSerializerGet
    permission_classes = [ReadOnly,]