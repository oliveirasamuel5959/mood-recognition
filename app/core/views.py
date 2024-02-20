from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, \
PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, \
update_session_auth_hash
#from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm
from .models import Users



def insert_user(userData):
    name = userData['username']
    email = userData['email']
    hashed_password = userData['password1']
    print(hashed_password)
    user = Users(username=name, email=email, password=hashed_password)
    user.save()
    
def check_user(userData):
    print(userData['username'])
    print(userData['password'])



# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')


def user_signup(request):
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            messages.success(request, 'Account created successfully!')
            #form.save()
            insert_user(form.cleaned_data)
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {
        'form': form,
    })
    

    
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST) 
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('/main/')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {
        'form': form,
    })
    

def user_logout(request):
    logout(request)
    return redirect('/')
        

    

