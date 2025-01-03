from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, 'You are now logged in')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid credentials')
            pass
    else:
        print("şifre yanlıs")
        return render(request, 'user/login.html')


def register(request):
    if request.method == 'POST':
        # Get form values
        username = request.POST['username']
        email = request.POST['mail']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            if User.objects.filter(username = username).exists():
                messages.add_message(request, messages.ERROR, 'Username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.add_message(request, messages.ERROR, 'Email is taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username = username, email = email, password = password)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'You are now registered and can log in')
                    return redirect('login')
                    
        else:
            messages.add_message(request, messages.WARNING, 'Passwords do not match')

        return redirect('register')
    else:
        return render(request, 'user/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, 'You are now logged out')
        return redirect('index')