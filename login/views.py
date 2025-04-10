from django.shortcuts import render
from django.contrib.auth.models import User, auth


# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        user= User.objects.create_user(username=username, password=password, email=email)
        user.save()
        print('User created')
        return render(request, 'login.html')

    else:
        return render(request, 'register.html')

