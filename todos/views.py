from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import TodoSerializer
from .models import Todos
from django_filters import rest_framework as df


class TodoFilter(df.FilterSet):
    completed = df.BooleanFilter(field_name='completed')
    priority = df.NumberFilter(field_name='priority')
    note = df.CharFilter(field_name='note', lookup_expr='icontains')
    project = df.CharFilter(field_name='project', lookup_expr='icontains')
    tags = df.CharFilter(field_name='tags__name', lookup_expr='icontains')
    due_date = df.DateFilter(field_name='due_date')
    share = df.CharFilter(field_name='share', lookup_expr='icontains')
    images = df.CharFilter(field_name='images', lookup_expr='icontains')
    references = df.CharFilter(field_name='references', lookup_expr='icontains')
    estimate = df.CharFilter(field_name='estimate', lookup_expr='icontains')
    note_array = df.CharFilter(field_name='note_array', lookup_expr='icontains')

    class Meta:
        model = Todos
        fields = ['completed', 'priority', 'note', 'project', 'tags', 'due_date',
                  'share', 'images', 'references', 'estimate', 'note_array']

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = TodoFilter
    ordering_fields = ['priority', 'due_date', 'creation_date']


def todo_list(request):
    return render(request, 'dt.html')
class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return all the latest todos."""
        return Todos.objects.order_by('creation_date')

def add(request):
    title = request.POST['title']
    Todos.objects.create(title=title)

    return redirect('todos:index')
def unique(request,param):
        return JsonResponse(list(Todos.objects.values_list(param, flat=True).distinct()),safe=False)

def delete(request, id):
    todo = get_object_or_404(Todos, pk=id)
    todo.delete()
    return redirect('todos:index')

def update(request, id):
    todo = get_object_or_404(Todos, pk=id)
    todo.completed = True if request.POST.get('completed', False)=="on" else False
    todo.save()
    return redirect('todos:index')