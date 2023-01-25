from django.urls import path

from . import views

# app_name = 'tasks'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('create/', views.TaskCreate.as_view(), name='task_create'),
    path('delete/<int:pk>/', views.TaskDelete.as_view(), name='task_delete'),
    path('update/<int:pk>/', views.TaskUpdate.as_view(), name='task_edit'),
    path('<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('tasks/', views.task_data, name='task_data'),
    path('calendar/', views.calendar, name='cal'),
]