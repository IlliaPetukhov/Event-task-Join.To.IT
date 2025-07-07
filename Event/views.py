from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .permissions import IsOwnderOrReadOnly
from rest_framework.permissions import IsAuthenticated
from User.models import EventJoiner
from EventManager.emails import send_email
from .serializers import EventSerializerGet, EventSerializerPostOrUpdateOrGetForOrganizerSerializer
from .models import Event
from datetime import date

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.select_related("organizer").all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title", "location_city", "date", "age_limit"]


    @action(detail=True, methods=["post"])
    def join(self, request, pk):
        
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        
        event = get_object_or_404(Event, id=pk)
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
        
        send_email(
            subject="Привіт друзяко, не звертай увагу це просто підтвердження що ми записали тебе на івент 🔥",
            message=f"Привіт! Це тестовий лист від нас який підтверджує що ми записали тебе на івент {event.title} за цією датою {event.date}", 
            recipient_list=[f"{user.email}"],
            user=user,
            action="join",
            event=event
        )
        
        return Response(
            {"detail": f"User {user.username} id {user.id} joined event {event.title} succesfully"},
            status=status.HTTP_200_OK
        )


    @action(detail=True, methods=["post"])
    def cancel(self, request, pk):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        user = request.user
        event = get_object_or_404(Event, id=pk)
        if user in event.user.all():
            event.user.remove(user)        
            return send_email(
                    subject=f"Привіт друзяко, не звертай увагу це просто підтвердження що ми відмінили твою участь у цьому івенті {event.title}",
                    message=f"Привіт! Це тестовий лист від нас який підтверджує що ми відмінили твою участь у цьому івенті {event.title} за цією датою {event.date}",
                    recipient_list=[f"{user.email}"],
                    user=user,
                    action="cancel",
                    event=event
                    )
        
        return Response({"detail": f"You are not longer participating in this event {event.title}"}, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return EventSerializerGet
    
        return EventSerializerPostOrUpdateOrGetForOrganizerSerializer
    
    def get_permissions(self):
        if self.action in ["join", "cancel", "create"]:
            return [IsAuthenticated(), ]
        return [IsOwnderOrReadOnly(), ]



    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

