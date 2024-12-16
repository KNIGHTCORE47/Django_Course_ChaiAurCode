from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Books(models.Model):
    GENRE_CHOICES = [
        ('S-FI', 'Sci-Fi'),
        ('ROM', 'Romance'),
        ('HOR', 'Horror'),
        ('COM', 'Comedy'),
        ('THR', 'Thriller'),
        ('FAN', 'Fantasy'),
        ('DRM', 'Drama'),
        ('FIC', 'Fiction'),
        ('NOV', 'Novel'),
        ('POE', 'Poetry'),
        ('ART', 'Art'),
        ('EVE', 'Eve'),
        ('HIS', 'History'),
        ('GEO', 'Geography'),
    ]

    name = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=100, default='')
    cover_image = models.ImageField(upload_to='uploads/')
    description = models.TextField(default='')
    pages = models.IntegerField(default=1)
    genre = models.CharField(max_length=4, choices=GENRE_CHOICES, default='S-FI')
    price = models.DecimalField(max_digits=10, default=0.00, decimal_places=2)

    def __str__(self):
        return self.name
    

### One to Many
class BookReview(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField(default='')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review for {self.book.name} by {self.user.username}"
    

### Many to Many
class BookStore(models.Model):
    store_name = models.CharField(max_length=100, default='')
    store_location = models.CharField(max_length=100, default='')
    collecton_of_books = models.ManyToManyField(Books, related_name='stores')

    def __str__(self):
        return self.store_name


### One to One
class BookNomination(models.Model):
    nomination_type = [
        ('NOM1', 'Nomination for best seller'),
        ('NOM2', 'Nomination for best author'),
        ('NOM3', 'Nomination for best genre'),
        ('NOM4', 'Nomination for best story'),
        ('NOM5', 'Nomination for best character'),
    ]

    book = models.OneToOneField(Books, on_delete=models.CASCADE, related_name='nomination')
    nomination_type = models.CharField(max_length=5, choices=nomination_type, default='NOM1')
    nomination_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Nomination for {self.book.name}is {self.nomination_type}"
    
