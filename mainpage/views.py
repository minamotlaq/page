from django.shortcuts import render
from django.http import HttpResponse
from .models import MainPage, Banner, Image


def home(request):
    pages = MainPage.objects.all()
    images = Image.objects.all() 
    return render(request, "mainpage/home.html", {"pages": pages, "images": images})



# from django.conf import settings
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse(settings.TEMPLATES[0]["DIRS"])

