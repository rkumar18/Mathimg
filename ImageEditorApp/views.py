from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image
from .models import Pic


def index(request):
    # img = img.rotate(180)
    # img.save("pages/rotated.jpg")
    return render(request, 'pages/index.html')


def img(request):
    return HttpResponse(Image.open("templates/pages/001.jpg"))
