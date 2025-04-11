from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def homepage(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

def login_view(request):
    if request.method == 'POST':
        username =request.POST['username']
        password= request.POST['password']

        user= auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
        

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return render(request, 'register.html')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return render(request, 'register.html')
            
            else:
                user= User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                print('User created')
                return redirect('login')
        else:
            print('password not matching')
            messages.info(request, 'Password not matching')
            return render(request, 'register.html')

    else:
        return render(request, 'register.html')

def logout_view(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('/')