from django.shortcuts import render

# Create your views here.
from .models import Login

def LoginView(request):
    return render(request, {})
