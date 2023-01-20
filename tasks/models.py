from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    STATUS_CHOICES = (
        ('not-started', 'not-started'),
        ('in-progress', 'in-progress'),
        ('in-review', 'in-review'),
        ('suspended', 'suspended'),
        ('completed', 'completed'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    assignee = models.ForeignKey(
        get_user_model(),
        related_name='assignee',
        on_delete=models.CASCADE,
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    
    class Meta:
        ordering = ('due_date',)

    def __str__(self):
        return self.name
