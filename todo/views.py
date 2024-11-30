from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Task


class TaskView(ListView):
    model = Task
    template_name = 'todo/tasks.html'
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    template_name = 'todo/task.html'
    context_object_name = 'task'

class TaskCreate(CreateView):
    model = Task
    template_name = 'todo/task_create.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class TaskEdit(UpdateView):
    model = Task
    template_name = 'todo/task_edit.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model = Task
    template_name = 'todo/task_delete.html'
    success_url = reverse_lazy('tasks')