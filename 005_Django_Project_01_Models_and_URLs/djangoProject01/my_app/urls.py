from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('cards/', views.cards, name='cards'),
    path('<int:params>', views.card_description, name='card_description'),
]