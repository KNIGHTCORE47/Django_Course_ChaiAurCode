from django.contrib import admin
from .models import Books, BookReview, BookStore, BookNomination 

# Register your models here.
class BookReviewInline(admin.TabularInline):
    model = BookReview
    extra = 2

class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'price')
    inlines = [BookReviewInline]

class BookStoreAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'store_location')
    filter_horizontal = ('collection_of_books',)


class BookNominationAdmin(admin.ModelAdmin):
    list_display = ('book', 'nomination_type', 'nomination_date')



admin.site.register(Books, BooksAdmin)
admin.site.register(BookStore, BookStoreAdmin)
admin.site.register(BookNomination, BookNominationAdmin)


