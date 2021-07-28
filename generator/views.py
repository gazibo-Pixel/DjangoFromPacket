from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html' )

def password(request):
    thepassword = ''
    chars = list('abcdefghijklmnopqrstxyz')
    length = 10
    for x in range(length):
        thepassword += random.choice(chars) 
    return render(request, 'generator/password.html', {'password': thepassword} )