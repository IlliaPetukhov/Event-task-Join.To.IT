from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from user.models import EventJoiner
from datetime import date
import re



class RegistrationSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateField(write_only=True)
    password = serializers.CharField(write_only=True, 
                                     style={
                                         "input_type": "password"
                                     }, 
                                     validators=[validate_password])
    
    class Meta:
        model = User
        fields = ["username", "email", "password", "date_of_birth"]

    
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already used")
        if not re.fullmatch(r"[a-z0-9_]+", value):
            raise serializers.ValidationError(
                "Username can only contain lowwercase letters, numbers, and underscores. No spaces or special characters."
            )
        return value


    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required field")
        
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already used")
        
        return value
    

    def validate_date_of_birth(self, value):
        if value >= date.today():
            raise serializers.ValidationError("This date is not acceptable")
        return value
        
    
    def create(self, validated_data):
        date_of_birth = validated_data.pop("date_of_birth")
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        EventJoiner.objects.create(date_of_birth=date_of_birth, user=user)
        return user


class LoginEmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, 
                                     style={
                                         "input_type": "password"
                                     } 
                                     )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop("username", None)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email.")
        
        authenticated_user = authenticate(username=user.username, password=password)
        if not authenticated_user:
            raise serializers.ValidationError("Invalid email or password")
        
        refresh = self.get_token(authenticated_user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }
    
    