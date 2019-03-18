from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from .models import User
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
# Create your views here.
def home(request):
	return render(request, 'home/home.html')

def welcome(request):
    return render(request, 'home/welcome.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register/register.html', {'form': form})

def profile(request):
    return render(request, 'profile/profile.html')

def admin(request):
    return render(request, 'admin/admin.html')


def updateProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile/updateProfile.html', context)

def log_in(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user.is_admin:
            return redirect('admin')
        else:
            login(request, user)
            if next:
                return redirect(next)
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'lilo/login.html', context)

# Create your views here.
def log_out(request):
	logout(request, User)
	return render(request, 'lilo/logout.html')
