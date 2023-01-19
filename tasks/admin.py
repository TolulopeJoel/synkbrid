from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'due_date', 'assignee', 'status']
    

admin.site.register(Task, TaskAdmin)
