from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm

def login_user(request):
    page = 'login'
    # 로그인된 상태로 접근할 때
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username OR password is incorrect')
    return render(request, 'users/login_register.html')

def logout_user(request):
    logout(request)
    messages.info(request, "User was logged out!")
    return redirect('login')

def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # 대소문자 구분안하기 위해!
            user.username  = user.username.lower()
            user.save()
            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'An error has occurred during registraion')

    context = {'page':page, 'form':form}
    return render(request, 'users/login_register.html', context)

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'users/profiles.html', context)

def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    top_skills = profile.skill_set.exclude(description__exact='')
    other_skills = profile.skill_set.filter(description='')

    context = {
        'profile':profile,
        'top_skills':top_skills,
        'other_skills':other_skills,
        }
    return render(request, 'users/user-profile.html', context)