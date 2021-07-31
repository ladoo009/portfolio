from django.shortcuts import render

from .models import Project


def home(request):
    return render(request, 'home.html')


def pro(request):
    p=Project.objects.all()
    print(p)
    return render(request, 'project.html',{'p':p})

def test(request):
    p = Project.objects.all()
    print(p)
    return render(request, 'pro_index.html',{'p':p})