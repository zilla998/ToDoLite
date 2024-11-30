from django.contrib import admin
from django.urls import path

from .views import TaskView, TaskCreate, TaskDetail, TaskEdit, TaskDelete

urlpatterns = [
    path('tasks/', TaskView.as_view(), name='tasks'),
    path('task-detail/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-edit/<int:pk>', TaskEdit.as_view(), name='task-edit'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete')
]
