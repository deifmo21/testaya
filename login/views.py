from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import Login

def index(request):

    username=request.POST.get('username')
    password=request.POST.get('Password')
    data=Login(name=username,passwords=password)
    
    return render(request,'login/index.html')