from rest_framework import serializers
from .models import Event




class EventSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["title", "description", "date", "location_city", "organizer", "age_limit"]


class EventSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["title", "description", "date", "location_city", "age_limit"]
