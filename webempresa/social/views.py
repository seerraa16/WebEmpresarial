from django.shortcuts import render
from .models import Link  # Cambiar Services por Link

# Create your views here.

def social(request):
    # Cambiar social.objects.all() a Link.objects.all()
    social_links = Link.objects.all()
    return render(request, "social/social.html", {'social': social_links})