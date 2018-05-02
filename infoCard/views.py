from django.shortcuts import render
from .models import Card

def info_list(request):
    cards = Card.objects.all()
    return render(request, 'infoCard/info_list.html', {'cards': cards})
