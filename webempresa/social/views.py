from django.shortcuts import render
from .models import Service

# Create your views here.

def social(request):
    social = social.objects.all()
    return render(request, "social/social.html",
{'social':social})