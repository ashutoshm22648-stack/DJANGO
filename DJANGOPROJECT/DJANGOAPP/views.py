from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    return render(request,'homePage.html')

def aboutus(request):
    return render(request,'aboutPage.html')

def view1(request):
    return HttpResponse("hello,World! This is view1.")

def sum(request):
    a = 12
    b = 56
    result = a + b
    return HttpResponse(f"The sum of {a} and {b} is {result}.")

# write a django view to print system date of the browser
def date(request):
    now1 =(datetime.datetime.now())
    return HttpResponse(now1)
