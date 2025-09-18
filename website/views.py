from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index_view(requset):
    return render(requset,'index.html')

def about_view(requset):
    return render(requset,'about.html')

def contact_view(requset):
    return render(requset,'contact.html')