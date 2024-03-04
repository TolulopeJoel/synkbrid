from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register('', views.TeamViewset, basename='team')

urlpatterns = router.urls
