from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django_filters.views import FilterView

from .filters import TaskFilter
from .forms import TaskForm
from .models import Task


class TaskListView(FilterView):
    model = Task
    template_name = 'tasks/task_list.html'
    filterset_class = TaskFilter


class TaskDetail(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Task


class TaskDelete(LoginRequiredMixin, generic.DeleteView):
    model = Task


class TaskCreate(LoginRequiredMixin, generic.CreateView):
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.assignee = self.request.user
        return super().form_valid(form)


# A JSON representation of tasks to display tasks on calendar
def task_data(request):
    tasks = Task.objects.all()
    task_list = []

    for task in tasks:

        # task status colors
        color = ''
        if task.status == 'in-progress':
            color = '#007bff'
        elif task.status == 'not-started':
            color = '#f44336'
        elif task.status == 'in-review':
            color = '#ffc107'
        elif task.status == 'suspended':
            color = '#6c757d'
        elif task.status == 'completed':
            color = '#28a745'

        task_list.append({
            'title': task.name,
            'start': task.start_date,
            'end': task.due_date,
            'color': color,
        })
    return JsonResponse(task_list, safe=False)


def calendar(request):
    return render(request, 'calendar.html')
