from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# from django.views.generic import ListView, DetailView # add these 

from django.http import HttpResponse
from django.urls import reverse
from .models import Horse, Training
from .forms import FeedingForm

class TrainingCreate(CreateView):
    model = Training
    fields = '__all__'

class TrainingList(ListView):
    model = Training

class TrainingDetail(DetailView):
    model = Training
    
class TrainingUpdate(UpdateView):
    model = Training
    fields = ['location', 'discipline']
    
    def get_success_url(self):
        return reverse('training-detail', kwargs={'pk': self.object.pk})
    
class TrainingDelete(DeleteView):
    model = Training
    success_url = '/trainings/'



class HorseCreate(CreateView):
    model = Horse
    fields = ['name', 'breed', 'description', 'age', 'grain_type']

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

class HorseUpdate(UpdateView):
    model = Horse
    fields = ['breed', 'description', 'age', 'grain_type']

class HorseDelete(DeleteView):
    model = Horse
    success_url = '/horses/'
    
def associate_training(request, horse_id, training_id):
    Horse.objects.get(id=horse_id).trainings.add(training_id)
    return redirect('horse-detail', horse_id=horse_id)


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
    trainings_horse_doesnt_have = Training.objects.exclude(id__in = horse.trainings.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'horses/detail.html', {
        'horse': horse, 'feeding_form': feeding_form, 'trainings': trainings_horse_doesnt_have
        })

def horse_index(request):
    horses = Horse.objects.all()
    return render(request, 'horses/index.html', {'horses': horses})


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

