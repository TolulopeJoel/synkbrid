from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import TaskForm
from .models import Task


class TaskList(generic.ListView):
    model = Task
    context_object_name = 'tasks'


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
