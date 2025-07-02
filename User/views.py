from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializerGet, UserSerializerPost

class UserViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
    
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return UserSerializerGet
        return UserSerializerPost
    
    