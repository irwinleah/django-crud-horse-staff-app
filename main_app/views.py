from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello 𓃗</h1>')

def about(request):
    return HttpResponse('<h1>About Horse Staff</h1>')