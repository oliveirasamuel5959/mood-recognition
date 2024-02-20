from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from .models import Users


def insert_user(userData):
    name = userData['username']
    email = userData['email']
    password = userData['password1']
    user = Users(username=name, email=email, password=password)
    user.save()
    
def check_user(userData):
    print(userData['username'])
    print(userData['password'])



# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            insert_user(form.cleaned_data)
            return redirect('/login/')
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {
        'form': form,
    })
    
    
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        check_user(form.cleaned_data)
        print('not')
        
        if form.is_valid():
            check_user(form.cleaned_data)
            return redirect('/')
    else:
        form = LoginForm()
        
    return render(request, 'core/login.html', {
        'form': form,
    })
        

    

