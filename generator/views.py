from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def about(requests):
    return render(requests, 'generator/about.html')


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvxwyz')

    lengh = int(request.GET.get('lengh', 12))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVXWYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special'):
        characters.extend(list('!#$%¨&*()/-+'))

    thepassword = ''

    for x in range(lengh):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
