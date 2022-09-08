from django.shortcuts import render

# Create your views here.
from .models import MyJob


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    my_job = MyJob.objects.get(pk=1)
    return render(request, 'index.html', context={'my_job': my_job},)
