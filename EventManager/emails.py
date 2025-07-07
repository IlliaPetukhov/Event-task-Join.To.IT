from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from decouple import config

def send_email(subject, message, recipient_list, user, event, action):
    try:   
        send_mail(
            subject=subject,
            message=message,
            from_email=config("EMAIL_HOST_USER"), 
            recipient_list=recipient_list,
        )
        if action == "join":
            return Response(
                {"detail": f"User {user.username} id {user.id} joined event {event.title} succesfully"},
                status=status.HTTP_200_OK
            )
        return Response({"detail": f"You canceled this event {event.title}"}, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"detail": f"Couldnt send an email: {e}"})