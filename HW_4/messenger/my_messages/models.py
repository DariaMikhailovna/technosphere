from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from chats.models import Chat


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')
    text = models.TextField(verbose_name='текст сообщения')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='дата создания')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='чат')

    def __str__(self):
        return self.text
