from django.shortcuts import render
from django.http import HttpResponse
from .models import Cuisine
# Create your views here.
def index(request):
    output=Cuisine.objects.all()
    return HttpResponse(output)
