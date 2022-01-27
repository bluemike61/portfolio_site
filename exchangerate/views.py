from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def exchangerate(request):
    return render(request, 'exchangerate/home.html')