from django.shortcuts import render

from django.http import HttpResponse

class Horse:
    def __init__(self, name, breed, description, age):
       self.name = name
       self.breed = breed
       self.description = description
       self.age = age


horses = [
    Horse('Star', 'Thoroughbred', 'Sweet.', 19),
    Horse('Fancy', 'Pony', 'Kinda rude.', 8 ),
    Horse('Beau', 'Appaloosa', 'charmer.', 8),
    Horse('Bandit', 'Quarter Horse', 'grumpy', 25),
    Horse('Holly', 'Hanovarian', 'Chill', 14),
    Horse('Poppy', 'Warmblood Cross', 'Big movement', 9),
]

def home(request):
    return HttpResponse('<h1>Hello 𓃗</h1>')

def about(request):
    return render(request, 'about.html')


def horse_index(request):
    return render(request, 'horses/index.html', {'horses': horses})