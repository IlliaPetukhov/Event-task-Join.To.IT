from rest_framework import serializers
from .models import Event
from django.contrib.auth.models import User


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class EventSerializerGet(serializers.ModelSerializer):
    organizer = OrganizerSerializer()
    class Meta:
        model = Event
        fields = ["id", "title", "description", "date", "location_city", "organizer", "age_limit"]



class EventSerializerPostOrUpdateOrGetForOrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["title", "description", "date", "location_city", "age_limit"]

