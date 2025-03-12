from django.shortcuts import render

from django.http import HttpResponse
from .models import Horse







def horse_index(request):
    horses = Horse.objects.all()
    return render(request, 'horses/index.html', {'horses': horses})

def horse_detail(request, horse_id):
    horse = Horse.objects.get(id=horse_id)
    return render(request, 'horses/detail.html', {'horse': horse})

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

