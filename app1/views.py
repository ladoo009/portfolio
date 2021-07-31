from django.shortcuts import render

# Create your views here.
from .models import home
def index(request):
    h= home.objects.all()
    print(h)
    return render(request, 'a.html',{'H':h})


def about(request):
    #h= home.objects.all()
    #print(h)
    return render(request, 'about1.html')