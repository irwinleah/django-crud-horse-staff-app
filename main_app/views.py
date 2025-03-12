from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic import ListView, DetailView # add these 

from django.http import HttpResponse
from .models import Horse
from .forms import FeedingForm



class HorseCreate(CreateView):
    model = Horse
    fields = ['name', 'breed', 'description', 'age']

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

class HorseUpdate(UpdateView):
    model = Horse
    fields = ['breed', 'description', 'age']

class HorseDelete(DeleteView):
    model = Horse
    success_url = '/horses/'
    
    
def add_feeding(request, horse_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.horse_id = horse_id
        new_feeding.save()
    return redirect('horse-detail', horse_id=horse_id)


# @login_required
def horse_detail(request, horse_id):
    horse = Horse.objects.get(id=horse_id)
    feeding_form = FeedingForm()
    return render(request, 'horses/detail.html', {
        'horse': horse, 'feeding_form': feeding_form
        })

def horse_index(request):
    horses = Horse.objects.all()
    return render(request, 'horses/index.html', {'horses': horses})


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

