from django.shortcuts import render

def accueil (request):
    return render(request, 'accueil.html')

def connexion (request):
    return render(request, 'connexion.html')

