from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'my_gene/home.html')

def password(request):

    character = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        character.extend(list('!@#$%^&*_'))

    if request.GET.get('numbers'):
        character.extend(list('1234567890'))

    length = int(request.GET.get('length',12))
    pass1 =''
    for x in range(length):
        pass1+= random.choice(character)

    return render(request,'my_gene/password.html',{'password':pass1})

def about(request):
    return render(request,'my_gene/about.html')
