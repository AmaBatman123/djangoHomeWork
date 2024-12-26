from django.shortcuts import render, redirect
from user.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, "user/register.html", context={"form": form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, "user/register.html", context={"form": form})
        elif form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password)
            return redirect("home")

def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, "user/login.html", context={"form": form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, "user/login.html", context={"form": form})
        elif form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            if not user:
                form.add_error(None, 'Username or password is incorrect')
                return render(request, "user/login.html", context={"form": form})

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect("home")