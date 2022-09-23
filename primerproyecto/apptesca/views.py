from django.shortcuts import render
from . import models
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def kevo(request):
    return render (request, 'prueba.html') 