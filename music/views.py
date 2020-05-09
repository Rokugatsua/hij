from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Song, Artist, Album

# Create your views here.

class Index(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'latest_song_list'

    def get_queryset(self):
        return Song.objects.order_by('-title')[:10]


class ListOn(generic.ListView):
    pass

class news(generic.ListView):
    pass

def artist_detail(request, artist_name):
    artist = get_object_or_404(Artist, name=artist_name)
    return render(request,'music/artists.html',{'artist': artist})


def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/album.html',{'albums':album})

