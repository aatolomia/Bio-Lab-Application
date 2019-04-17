from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import View, CreateView
from django.contrib.auth.decorators import login_required
from .forms import ( UserRegisterForm, UserLoginForm, UserUpdateForm, ProfileUpdateForm,
adminloginform, adminupdateform, adminprofileupdateform, AdminDetailsForm)
from .models import User
from student.models import Notification
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
    user = request.user
    return render(request, 'profile/profile.html',{'user': user})

def admin(request):
    return render(request, 'admin/admin.html')

def credentials(request):
    return render(request, 'home/credentials.html')

@login_required
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

def notification(request):
    return render(request, 'home/home.html')

def adminprofile(request):
    user = request.user
    return render(request, 'admin/adminprofile.html',{'user': user})

def adminsite(request):
    return render(request, 'admin/adminsite.html')


def adminhome(request):
    return render(request, 'Admin/AdminHome/adHome.html')

def updateAdmin(request):
    if request.method == 'POST':
        u_form = adminupdateform(request.POST, instance=request.user)
        p_form = adminprofileupdateform(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            user = p_form.save()
          #  login(request, user, backend='django.contrib.auth.backends.ModelBackend')
      
           # messages.success(request, f'Your account has been updated!')
            return redirect('adminprofile')
    else:
        u_form = adminupdateform(instance=request.user)
        p_form = adminprofileupdateform(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'admin/adminprofile.html', context)


def adminlogout(request):
    return render(request, 'admin/adminlogout.html')

def adminlogin(request):
    next = request.GET.get('next')
    form = adminloginform(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email = email, password = password)
        if user.is_admin:
            if next:
                return redirect(next)
            return redirect('adminhome')
        else:
            messages.error(request, 'This is not the site for student login.')
            

    context = {
        'form': form,
    }
    return render(request, 'admin/adminlogin.html', context)




def admindetails(request):
    if request.method == 'POST':
        user_form = AdminDetailsForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            #.set_password(user.password)
            user.save()
            #email = form.cleaned_data.get('email')
           #
            return redirect('adminhome')
    else:
        form = AdminDetailsForm()
    return render(request, 'admin/admindetails.html', {'form': form})

