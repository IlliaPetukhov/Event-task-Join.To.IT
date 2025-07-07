from rest_framework import serializers
from django.contrib.auth.models import User
from Event.serializers import EventSerializerPostOrUpdateOrGetForOrganizerSerializer, EventSerializerGet 
from User.models import EventJoiner
from Event.models import Event
from datetime import date
from django.contrib.auth.password_validation import validate_password



class UserSerializerPost(serializers.ModelSerializer):
    date_of_birth = serializers.DateField(write_only=True)
    password = serializers.CharField(write_only=True, 
                                     style={
                                         "input_type": "password"
                                     }, 
                                     validators=[validate_password])
    class Meta:
        model = User
        fields = ["username", "email", "password", "date_of_birth"]

    def validate(self, attrs):
        date_of_birth = attrs.get("date_of_birth")
        email = attrs.get("email")
        if not email:
            raise serializers.ValidationError({"email": "Email is required field"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "This email is already used"})
        if date.today() <= date_of_birth:
            raise serializers.ValidationError({"date_of_birth": "This date is not acceptable"})
        return attrs

    
    def create(self, validated_data):
        date_of_birth = validated_data.pop("date_of_birth")
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        EventJoiner.objects.create(date_of_birth=date_of_birth, user=user)
        return user




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
        