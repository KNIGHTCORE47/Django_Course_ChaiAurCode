from django.shortcuts import render
from .models import Books, BookStore
from .forms import BookForm

# Create your views here.
def store(request):
    all_books = Books.objects.all()
    return render(request, 'website/store.html', {'products': all_books})

def book_availablity(request):
    drop_down = None
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book_genre = form.cleaned_data['book_list']
            drop_down = BookStore.objects.filter(collection_of_books=book_genre)
    else:
        form = BookForm()

    return render(request, 'website/book_availablity.html', {'drop_down': drop_down,'form': form})
