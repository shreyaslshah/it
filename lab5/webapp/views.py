from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hello(request):
    return render(request, 'hello.html')

def q1(request):
    return render(request, 'q1.html')

def q2(request):
    return render(request, 'q2.html')

def q3(request):
    return render(request, 'q3.html')

def q4(request):
    return render(request, 'q4.html')