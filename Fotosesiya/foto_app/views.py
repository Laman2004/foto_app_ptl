from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'foto_app/index.html')

def about(request):
    return render(request,'foto_app/about.html')

def registration(request):
    return render(request,'foto_app/about.html')

# Create your views here.
