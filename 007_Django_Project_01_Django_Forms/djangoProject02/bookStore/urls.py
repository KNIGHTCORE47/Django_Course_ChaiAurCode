from django.urls import path, include
from . import views

urlpatterns = [
    path('store/', views.store, name='store'),
    path('book_availablity/', views.book_availablity, name='book_availablity'),
]