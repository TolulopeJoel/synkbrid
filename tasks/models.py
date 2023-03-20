from django.db import models

from accounts.models import Team


class Task(models.Model):
    STATUS_CHOICES = (
        ('not-started', 'not-started'),
        ('in-progress', 'in-progress'),
        ('in-review', 'in-review'),
        ('suspended', 'suspended'),
        ('completed', 'completed'),
    )
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('due_date',)

    def __str__(self):
        return self.name
