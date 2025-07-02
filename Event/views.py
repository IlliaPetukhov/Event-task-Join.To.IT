from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from User.models import EventJoiner
from .serializers import EventSerializerGet, EventSerializerPost
from .models import Event
from datetime import date

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()

    @action(detail=True, methods=["post"])
    def join(self, request, pk):
        event = Event.objects.get(id=pk)
        user = request.user
        if user in event.user.all():
            return Response({"detail": "You are already joined this event"}, status=status.HTTP_400_BAD_REQUEST)
        
        if event.age_limit:
            today = date.today()
            date_of_birth = EventJoiner.objects.get(user=user).date_of_birth

            if (today.year - date_of_birth.year - ((date_of_birth.month, date_of_birth.day) > (today.month, today.day))) < 18:
                return Response(
                    {"detail": f"User {user.username} id {user.id} tried to join 18+ event {event.id} but he is younger"},
                    status=status.HTTP_406_NOT_ACCEPTABLE
                )
            
        event.user.add(user)
        return Response(
            {"detail": f"User {user.username} id {user.id} joined event {event.title} succesfully"},
            status=status.HTTP_200_OK
        )

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return EventSerializerGet
        return EventSerializerPost
    
    
    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)