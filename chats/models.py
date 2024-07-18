from django.db import models
from django.utils import timezone


class Message(models.Model):
    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='messages',
    )
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
