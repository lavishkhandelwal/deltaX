from django.shortcuts import redirect
from .models import Ratings
from songs.models import Song
from artists.models import Artist

def rate_song(request):
    if request.method == 'POST':
        val = request.POST.get('rating')
        song_id = request.POST.get('songId')
        user = request.user
        song = Song.objects.get(id = song_id)
        rating = Ratings.objects.filter(song = song, user = user)
        if not rating.exists():
            rating = Ratings.objects.create(song = song, user = user, rating = val)
        else:
            rating.update(rating = val)
        rating = Ratings.objects.filter(song = song).values()
        total = 0
        for r in rating:
            total += r['rating']
        song = Song.objects.get(id = song_id)
        song.total = rating.count()
        song.rate = total / song.total
        song.save()
        artists = song.artist.all().values()
        for artist in artists:
            total = 0.0
            total_song = Song.objects.filter(artist = artist['id']).values()
            for song in total_song:
                total = max(song['rate'], total)
            curr_artist = Artist.objects.get(id = artist['id'])
            curr_artist.rate = total
            curr_artist.save()
        return redirect('songs') 
    return redirect('songs')