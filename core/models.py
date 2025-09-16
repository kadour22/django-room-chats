from django.db import models
from django.contrib.auth.models import User


class Room(models.Model) :
    name = models.CharField(max_length=255)

class Message(models.Model) :
    room      = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    content   = models.CharField()
    timestamp = models.DateTimeField(auto_now_add=True)