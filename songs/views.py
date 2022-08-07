from artists.models import Artist
from .models import Song
from django.shortcuts import render
from django.http import JsonResponse
from ratings.models import Ratings

# Create your views here 
def index(request):
    user = request.user
    songs = Song.objects.all().order_by('-rate')
    return render(request, 'songs.html', {'songs': songs})

def add(request):
    artists = Artist.objects.all().order_by('name')
    if request.method == 'POST':
        name = request.POST.get('songname', None)
        dor = request.POST.get('date', None)
        artwork = request.FILES.get('artwork', None)
        artist = request.POST.get('artistInput', None)
        print(name, dor, artwork, artist)
        if name and dor and artwork and artist:
            if Song.objects.filter(name = name, dor = dor).exists():
                return JsonResponse({'msg': 0})
            song = Song.objects.create(name = name, dor = dor, cover = artwork, rate = 0)
            for a in artist.split(','):
                song.artist.add(Artist.objects.get(name = a))
            return JsonResponse({'msg' : 'Save'})
        else:
            return JsonResponse({'msg': "fill all fields"})
    return render(request, 'add song.html', {'artists': artists})