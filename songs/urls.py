from django.urls import path
from .views import *
from artists.views import ajax_artists
from ratings.views import rate_song

urlpatterns = [
    path('', index, name = 'songs'),
    path('add/', add, name = 'add'),
    path('rate/', rate_song, name = 'rate'),
    path('add/ajax_artists/', ajax_artists, name = 'ajax_artists'),
]
