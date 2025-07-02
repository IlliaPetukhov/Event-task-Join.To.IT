from django.shortcuts import render
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializerGet

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return EventSerializerGet
        return EventSerializerGet