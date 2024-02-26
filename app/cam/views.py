from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import InputImageForm

# Create your views here.
def main_view(request):
    return render(request, 'cam/main.html')
        

    
    

