from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import InputImageForm

# Create your views here.
def main_view(request):
    if request.method == 'POST':
        form = InputImageForm(request.POST)
    else:
        form = InputImageForm()
        
    return render(request, 'cam/main.html', {
        'form': form,
    })
