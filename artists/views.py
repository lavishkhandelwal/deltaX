from django.shortcuts import render
from django.http import JsonResponse
from .models import Artist

# Create your views here.
def index(request):
    artists = Artist.objects.all().order_by('-rate', 'name')
    return render(request, 'artists.html', {'artists': artists})

def ajax_artists(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        dob = request.POST.get('dob', None)
        bio = request.POST.get('bio', None)
        if name and dob and bio:
            if Artist.objects.filter(name = name, dob = dob).exists():
                return JsonResponse({'msg': 0})
            new_artist = Artist(name=name, dob=dob, bio=bio)
            new_artist.save()
            artists = Artist.objects.all().order_by('name').values()
            artists_data = list(artists)
            return JsonResponse({'msg' : 'Save', 'artists_data' : artists_data})
        else:
            return JsonResponse({'msg': "fill all fields"})
