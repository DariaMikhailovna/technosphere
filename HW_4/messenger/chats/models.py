from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Chat(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created', verbose_name='автор')
    title = models.CharField(max_length=200, verbose_name='название чата')
    participants = models.ManyToManyField(User, verbose_name='получатели')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
