from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def paginaweb(request):
    return HttpResponse("Hi")