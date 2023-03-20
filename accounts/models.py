from django.db import models
from django.contrib.auth import get_user_model


class Team(models.Model):
    name = models.CharField(max_length=225)
    teamates = models.ManyToManyField(get_user_model())
    assigner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='assigner')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
