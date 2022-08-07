from nturl2path import url2pathname
from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name = 'artists'),
]
