from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("hola!")
    return render(request,"home.html")