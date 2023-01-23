import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    # status = django_filters.CharFilter(field_name='status', lookup_expr='exact')

    class Meta:
        model = Task
        fields = ['status']
