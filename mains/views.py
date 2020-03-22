from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
def home(request):
    return render(request , 'base.html')


def new_search(request):
    search = request.POST.get('search')
    stuff_for_frontend = {
        'search' : search,
    }
    return render(request , 'mains/new_search.html' , stuff_for_frontend)
# Create your views here.
