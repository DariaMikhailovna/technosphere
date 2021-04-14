from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from chats.models import Chat


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    def send(self):
        self.save()

    def __str__(self):
        return self.text
