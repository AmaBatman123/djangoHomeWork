from django.shortcuts import render
from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Hello World!")

def html_view(request):
    return render(request, "base.html")
