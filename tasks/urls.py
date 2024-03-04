from django.urls import path

from . import views


urlpatterns = [
    path('', views.TaskList.as_view(), name='task-list'),
    path('<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
]
