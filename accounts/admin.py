from django.contrib import admin

from .models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'assigner', 'created_at']

admin.site.register(Team, TeamAdmin)
