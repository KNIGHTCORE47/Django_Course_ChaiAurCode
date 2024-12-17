from django import forms
from .models import Books, BookReview, BookStore, BookNomination


class BookForm(forms.Form):
    book_list = forms.ModelChoiceField(queryset=Books.objects.all(), label='Book Available')