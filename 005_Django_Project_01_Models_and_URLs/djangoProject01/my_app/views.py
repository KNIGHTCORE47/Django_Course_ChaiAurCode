from django.shortcuts import render


def about(request):
    return render(request, 'website/about.html')

def cards(request):
    return render(request, 'website/cards.html')
