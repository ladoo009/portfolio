from django.shortcuts import render


from .models import Intex


def info(request):
    l= Intex.objects.all()
    print(l)
    return render(request, 'b.html',{'L': l})



def about1(request):
    #h= home.objects.all()
    #print(h)
    return render(request, 'about1.html')

