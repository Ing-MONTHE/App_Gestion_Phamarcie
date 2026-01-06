from django.shortcuts import render
from .models import *

def home(request):
    #recuperation des donnees
    donnees = Produit.objects.all()
    context = {
        'donnees': donnees
    }
    
    return render(request, 'home.html', context)