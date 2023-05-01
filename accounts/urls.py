from django.urls import path
from rest_framework.routers import SimpleRouter

from rest_framework_simplejwt import views as jwt_views


from . import views

urlpatterns = [
    path('auth/login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', views.RegisterView.as_view(), name='register'),
]

router = SimpleRouter()

router.register('teams', views.TeamViewset, basename='team')


urlpatterns += router.urls
