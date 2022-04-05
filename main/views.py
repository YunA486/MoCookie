from django.http import HttpResponse
from django.shortcuts import render

# def say_hello(request):
#     return HttpResponse("Hello, World!")

def firstpage(request):
    return render(request, 'first.html')

def secondpage(request):
    return render(request, 'second.html')

def thirdpage(request):
    return render(request, 'third.html')