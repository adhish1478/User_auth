from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                message='Username already exists'
                messages.info(request, 'Username already exists')
                return render(request, 'register.html')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                message='Email already exists'
                return render(request, 'register.html')
            
            else:
                user= User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                print('User created')
                return render(request, 'login.html')
        else:
            print('password not matching')
            messages.info(request, 'Password not matching')
            return render(request, 'register.html')

    else:
        return render(request, 'register.html')

