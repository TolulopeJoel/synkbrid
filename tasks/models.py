from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    STATUS_CHOICES = (
        ('on hold', 'on hold'),
        ('completed', 'completed'),
        ('in review', 'in review'),
        ('not started', 'not started'),
        ('in progress', 'in progress'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    assignee = models.ForeignKey(
        get_user_model(),
        related_name='assignee',
        on_delete=models.CASCADE,
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self) -> str:
        return self.name
