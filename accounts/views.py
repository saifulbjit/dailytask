from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def login(request):
    if request.user.is_authenticated:
        messages.error(request, 'You\'re already logged in')
        return redirect('jobs:homepage')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('jobs:homepage')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')


@login_required()
def logout(request):
    messages.success(request, "Logout successful")
    auth_logout(request)
    return redirect('jobs:homepage')


def register(request):
    if request.user.is_authenticated:
        messages.error(request, 'Cannot register as you\'re already logged in')
        return redirect('jobs:homepage')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('accounts:login')
        else:
            messages.error(request, 'There was an error with your registration. Please try again.')

    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})
