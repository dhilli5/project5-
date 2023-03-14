from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_first(request):
    return HttpResponse("<h2><marquee> this is my app2 first function</marquee></h2>")


def app2_second(request):
    return HttpResponse("<h2><marquee> this is my app2 second  function</marquee></h2>")

def app2_third(request):
    return HttpResponse("<h2> This is my app2 third function</h2>")
    


