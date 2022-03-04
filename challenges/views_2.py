from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("Eat more eat, eggs and vegetables")  # The argument of this method is the
    # data we want to send to the client
    # Here we want to return the response (HttpResponse that we imported with the django.http module) 
    # that is going to be sent back to the client (the browser sending the request)
    # Django will execute this function for us when this request hits the Django server
    # Creating an urls.py file so that Django can use them as arguments

def february(request):
    return HttpResponse("Lift weights at least 4 times a week for 40 minutes.")

def march(request):
    return HttpResponse("Learn Python Django for one hour every day.")

def monthly_challenge(request):
    return HttpResponse()