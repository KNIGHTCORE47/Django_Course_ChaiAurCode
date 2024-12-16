from django.shortcuts import render
from .models import Books

# Create your views here.
def store(request):
    all_books = Books.objects.all()
    return render(request, 'website/store.html', {'products': all_books})
