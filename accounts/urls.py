from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

urlpatterns = [
    path('auth/login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/register/', views.RegisterView.as_view(), name='register'),
]

router = SimpleRouter()

router.register('teams', views.TeamViewset, basename='teams')


urlpatterns += router.urls
