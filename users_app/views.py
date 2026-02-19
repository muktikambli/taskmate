from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import CreateUserForm


def register(request):
    if request.method == 'POST':
        registerform = CreateUserForm(request.POST)
        if registerform.is_valid():
            registerform.save()
            messages.success(request, "User Registration Successful! Login to get started.")
            return redirect('register')
    else:      
        registerform = CreateUserForm()
    return render(request, 'users_app/register.html', {'registerform': registerform})

def logout_view(request):
    logout(request)
    request.session.flush()  # Clear all session data
    messages.success(request, "You have been logged out successfully.")
    return render(request, 'users_app/logout.html')