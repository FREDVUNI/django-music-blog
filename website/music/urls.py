from django.urls import path
from . import views

app_name ="music"

urlpatterns=[
    path("",views.IndexView.as_view(),name="index"),
    path("<str:slug>",views.DetailView.as_view(),name="detail"),
    path("add/album",views.createAlbum.as_view(),name="addAlbum"),
    path("<str:slug>/album/update",views.updateAlbum.as_view(),name="updateAlbum"),
    path("<str:slug>/album/delete",views.deleteAlbum.as_view(),name="deleteAlbum"),

    path("add/song",views.createSong.as_view(),name="addSong"),
    path("<int:pk>/song/update",views.updateSong.as_view(),name="updateSong"),
    path("all/songs",views.allSongs.as_view(),name="songs"),
    path("<int:album_id>/favorite",views.favorite,name="favorite"),
    path("search/album",views.search,name="search")

    #path("",views.index,name="index"),
    #path("<int:album_id>/details",views.detail,name="detail"),
    #path("<int:album_id>/favorite",views.favorite,name="favorite"),
]