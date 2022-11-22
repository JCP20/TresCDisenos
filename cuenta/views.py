from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mosaico(request):
    return render(request,'mosaico.html')