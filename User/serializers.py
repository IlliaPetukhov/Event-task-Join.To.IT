from rest_framework import serializers
from django.contrib.auth.models import User
from Event.serializers import EventSerializerGet


class UserSerializerPost(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, 
                                     style={
                                         "input_type": "password"
                                     })
    class Meta:
        model = User
        field = ["username", "email", "password"]


class UserSerializerGet(serializers.ModelSerializer):
    events = EventSerializerGet(read_only=True)
    class Meta:
        model = User
        field = ["username", "email", "events"]
