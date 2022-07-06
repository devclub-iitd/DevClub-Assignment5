from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def bye(request):
    return HttpResponse("Bye World!")

def hi(request, name):
    return render(request, 'hi.html', {'name': name})