from .models import Team


class UserTeamQueryset():
    """
    Queryset class for retrieving teams where the current user is a teamate.
    """

    def get_queryset(self):
        """
        Get queryset of teams where the current user is a teamate.

        Returns:
            Queryset of Team objects filtered by the current user being a teamate.
        """
        user = self.request.user
        return Team.objects.filter(teamates=user)
