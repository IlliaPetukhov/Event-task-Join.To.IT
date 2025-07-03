from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User
from .serializers import UserSerializerGet, UserSerializerPost

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