from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from . models import Album,Song
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.db.models import Q

# Create your views here.
class IndexView(generic.ListView):
    template_name ="music/index.html"
    context_object_name ="albums"

    def get_queryset(self):
        return Album.objects.order_by('-album_title')

class DetailView(generic.DetailView):
    model = Album
    template_name ="music/details.html"      

class createAlbum(CreateView):
    model =Album
    fields=["artist","album_title","genre","slug","album_logo"]

class updateAlbum(UpdateView):
    model =Album
    fields=["artist","album_title","genre","slug","album_logo"] 

class deleteAlbum(DeleteView):
    model = Album
    success_url =reverse_lazy("music:index")

class createSong(generic.CreateView):
    model = Song
    fields =["album","file_type","song_title"]

class updateSong(generic.UpdateView):
    model = Song
    fields =["album","file_type","song_title"] 

class allSongs(generic.ListView):
    context_object_name ="songs"
    template_name ="music/songs.html"

    def get_queryset(self):
        return Song.objects.all()

class searchQuery(generic.ListView):
    template_name="music/search.html"

    def get_queryset(self):
        query = self.request.GET.get('q' or None)
        albums = Album.objects.filter(album_title__icontains = query)
        return albums

def favorite(request,album_id):
    album = get_object_or_404(Album,pk=album_id)

    template ="music/details.html"
    context ={"album":album}

    try:
        song = album.song_set.get(pk = request.POST['song_id'])
    except(KeyError,Song.DoesNotExist):
         return render(request,template,context)
    else:
        if song.is_favorite == False:
            song.is_favorite = True
            song.save()
        else:
            song.is_favorite = False
            song.save()
        return render(request,template,{"album":album})  

def search(request):
    query = request.GET.get('q',None)
    if query is not None:
        albums = Album.objects.filter(Q(album_title__icontains = query)|
        Q(artist__icontains = query)|Q(genre__icontains = query))
        context ={"albums":albums}
        
    return render(request,"music/search.html",context)


#def index(request):
#    albums =Album.objects.all()
#    template ="music/index.html"
#    context={"albums":albums}
#    return render(request,template,context)


#def detail(request, album_id):
#    album = get_object_or_404(Album,pk=album_id)
#    template ="music/details.html"
#    context={"album":album}
#    return render(request,template,context)


#def favorite(request, album_id):
#    album = get_object_or_404(Album,pk=album_id)
#    template ="music/details.html"
#    context={"album":album}

#    try:
#        song = album.song_set.get(pk = request.POST['song'])
#    except(KeyError,Song.DoesNotExist):    
#        return render(request,template,{
#            "album":album,
#            "error_message":"The song seems to te Invalid.",
#        })
#    else:
#        if song.is_favorite == False:
#            song.is_favorite = True
#            song.save()
#        else:
#            song.is_favorite = False
#            song.save()
#        return render(request,template,{"album":album})


