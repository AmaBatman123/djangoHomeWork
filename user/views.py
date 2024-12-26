from django.shortcuts import render, redirect
from user.forms import RegisterForm
from django.contrib.auth.models import User

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