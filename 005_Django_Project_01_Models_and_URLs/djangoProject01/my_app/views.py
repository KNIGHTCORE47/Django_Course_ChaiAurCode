from django.shortcuts import render
from .models import ChaiVariety


def about(request):
    return render(request, 'website/about.html')

def cards(request):
    all_chais = ChaiVariety.objects.all()   # Output: It gonna be a List of ChaiVariety Objects
    return render(request, 'website/cards.html', {'all_chais': all_chais})    # NOTE - here we send the list of ChaiVariety Objects with the help of jinja2
