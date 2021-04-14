from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name='владелец')
    status = models.TextField(verbose_name='статус')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='дата создания')

    def __str__(self):
        pass
