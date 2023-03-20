from .models import Team

class UserTeamQueryset():
    def get_queryset(self):
        queryset = Team.objects.all()
        user = self.request.user
        user_queryset = []

        for team in queryset:
            teamates = team.teamates.all()
            if user in teamates:
                user_queryset.append(team)
        
        return user_queryset