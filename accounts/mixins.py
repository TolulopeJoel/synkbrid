from .models import Team


class UserTeamQueryset():
    def get_queryset(self):
        user = self.request.user
        return Team.objects.filter(teamates=user)
