from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.views import LoginView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

from .models import Horse, Training

from .forms import FeedingForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm




def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('horse-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)





# @login_required
def remove_training(request, horse_id, training_id):
    horse = Horse.objects.get(id=horse_id)
    training = Training.objects.get(id=training_id)
    horse.trainings.remove(training_id)
    return redirect('horse-detail', horse_id=horse.id)

@login_required
def associate_training(request, horse_id, training_id):
    Horse.objects.get(id=horse_id).trainings.add(training_id)
    return redirect('horse-detail', horse_id=horse_id)

class TrainingCreate(LoginRequiredMixin, CreateView):
    model = Training
    fields = '__all__'

class TrainingList(LoginRequiredMixin, ListView):
    model = Training

class TrainingDetail(LoginRequiredMixin, DetailView):
    model = Training
    
class TrainingUpdate(LoginRequiredMixin, UpdateView):
    model = Training
    fields = ['location', 'discipline']
    
    def get_success_url(self):
        return reverse('training-detail', kwargs={'pk': self.object.pk})
    
class TrainingDelete(LoginRequiredMixin, DeleteView):
    model = Training
    success_url = '/trainings/'







class HorseUpdate(LoginRequiredMixin, UpdateView):
    model = Horse
    fields = ['breed', 'description', 'age', 'grain_type']

class HorseDelete(LoginRequiredMixin, DeleteView):
    model = Horse
    success_url = '/horses/'

class HorseCreate(LoginRequiredMixin, CreateView):
    model = Horse
    fields = ['name', 'breed', 'description', 'age', 'grain_type']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
@login_required
def horse_detail(request, horse_id):
    horse = Horse.objects.get(id=horse_id)
    trainings_horse_doesnt_have = Training.objects.exclude(id__in = horse.trainings.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'horses/detail.html', {
        'horse': horse, 'feeding_form': feeding_form, 'trainings': trainings_horse_doesnt_have
        })

@login_required
def add_feeding(request, horse_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.horse_id = horse_id
        new_feeding.save()
    return redirect('horse-detail', horse_id=horse_id)


    
@login_required
def horse_index(request):
    horses = Horse.objects.filter(user=request.user)
    horse = request.user.horse_set.all()
    return render(request, 'horses/index.html', {'horses': horses})






class Home(LoginView):
    template_name = 'home.html'




def about(request):
    return render(request, 'about.html')

