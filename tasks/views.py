from django.http import JsonResponse
from django_filters.views import FilterView

from .models import Task


from rest_framework import viewsets
from .serializers import TaskSerializer


class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    # def get_queryset(self):
    #     user = self.request.user
    #     return super().get_queryset().filter(assignee=user)




# # A JSON representation of tasks to display tasks on calendar
# def task_data(request):
#     tasks = Task.objects.all()
#     task_list = []

#     for task in tasks:

#         # task status colors
#         color = ''
#         if task.status == 'in-progress':
#             color = '#007bff'
#         elif task.status == 'not-started':
#             color = '#f44336'
#         elif task.status == 'in-review':
#             color = '#ffc107'
#         elif task.status == 'suspended':
#             color = '#6c757d'
#         elif task.status == 'completed':
#             color = '#28a745'

#         task_list.append({
#             'title': task.name,
#             'start': task.start_date,
#             'end': task.due_date,
#             'color': color,
#         })
#     return JsonResponse(task_list, safe=False)


# def calendar(request):
#     return render(request, 'calendar.html')
