from django.shortcuts import render
from .models import *

# Create your views here.
def informaions(request):
    data = info.objects.all()
    return render(request, "contet.html", {"data": data})
