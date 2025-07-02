from django.shortcuts import render
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializerGet, EventSerializerPost

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return EventSerializerGet
        return EventSerializerPost
    
    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)