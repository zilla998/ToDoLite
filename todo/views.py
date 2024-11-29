from django.shortcuts import render
from django.views.generic import ListView


def TodoHome(request):
    return render(request, 'todo/index.html')
