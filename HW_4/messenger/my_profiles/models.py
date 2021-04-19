from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='владелец')
    status = models.TextField(verbose_name='статус', blank=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name='дата создания')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
