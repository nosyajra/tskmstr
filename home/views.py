from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')

# Create your views here.

def home(request):
    return render(request, 'home.html')
