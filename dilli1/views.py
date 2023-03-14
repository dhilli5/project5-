from django.shortcuts import render
from django.http import HttpResponse


def dilli1_first(request):
    return HttpResponse('<h1> this is my fisrt function')
def dilli1_second(request):
    return HttpResponse("<h1> this is my second function</h1>")

# Create your views here.
