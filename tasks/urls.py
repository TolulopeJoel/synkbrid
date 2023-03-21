from django.urls import path

from . import views


urlpatterns = [
    path('tasks/', views.TaskList.as_view(), name='tasks-list'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='tasks-detail'),
]
