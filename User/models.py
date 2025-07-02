from django.db import models
from django.contrib.auth.models import User

class EventJoiner(models.Model):
    date_of_birth = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return f"{self.user.username}, {self.date_of_birth}"
