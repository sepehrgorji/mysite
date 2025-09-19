from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index_view(requset):
    return render(requset,'website/index.html')

def about_view(requset):
    return render(requset,'website/about.html')

def contact_view(requset):
    return render(requset,'website/contact.html')