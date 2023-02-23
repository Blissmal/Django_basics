import datetime
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h2>Now time is %s.</h2></body></html>" % now
    return HttpResponse(html)


def welcome(request):
    return HttpResponse("Welcome to Django class")


def greeting(request):
    html = "<html><body><h1>Greeting from bliss productions</h1><p>We have a new program ...<p></body></html>"
    return HttpResponse(html)


def info(request):
    return HttpResponse("We are now available through various website platforms")


def emobilis(request):
    return HttpResponse("eMobilis mobile Technology")


def home(request):
    return render(request, 'home.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')


def intro(request):
    return render(request, 'Intro.html')
