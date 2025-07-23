from rest_framework import serializers
from django.contrib.auth.models import User
from event.serializers import EventSerializerPostOrUpdateOrGetForOrganizerSerializer, EventSerializerGet 



class UserSerializerGet(serializers.ModelSerializer):
    joined_event = EventSerializerGet(many=True)
    class Meta:
        model = User
        fields = ["username", "email", "joined_event"]
    



class OrganizerSerializerGet(serializers.ModelSerializer):
    organized_events = EventSerializerPostOrUpdateOrGetForOrganizerSerializer(source="organizer", many=True)
    class Meta:
        model = User
        fields = ["username", "email", "organized_events"] 
        