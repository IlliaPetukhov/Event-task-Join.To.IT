from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from event.permissions import ReadOnly
from .models import User
from .serializers import UserSerializerGet, OrganizerSerializerGet


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializerGet
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "put", "delete", "patch"]
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
    
 
    
class OrganizerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.prefetch_related("organizer").all()
    serializer_class = OrganizerSerializerGet
    permission_classes = [ReadOnly,]