from django.shortcuts import render

def connexion (request):
    return render(request, 'compte/connexion.html')

