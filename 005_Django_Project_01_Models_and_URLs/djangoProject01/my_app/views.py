from django.shortcuts import render, get_object_or_404
from .models import ChaiVariety


def about(request):
    return render(request, 'website/about.html')

def cards(request):
    all_chais = ChaiVariety.objects.all()   # Output: It gonna be a List of ChaiVariety Objects
    return render(request, 'website/cards.html', {'all_chais': all_chais})    # NOTE - here we send the list of ChaiVariety Objects with the help of jinja2


def card_description(request, params):
    # pk = primary key
    card_id = get_object_or_404(ChaiVariety, pk=params)
    return render(request, 'website/card_description.html', {'card_id': card_id})