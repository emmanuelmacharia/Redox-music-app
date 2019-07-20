#create another url file to make sure the main urls.py in (Music project) isn't too cluttered
#we import the urls from here to the main routing file
from django.conf.urls import url
from . import views #.-means same directory
from django.views.generic import ListView, DetailView
#from music import views
from music.models import Albums, Songs
from rest_framework.urlpatterns import format_suffix_patterns
app_name='music'

#urlpatterns = [
#    url(r'^(?P<id>\d+)/$', views.albumdetails, name='albumdetails'), #/music/20/
#    url(r'^$', views.index, name='index'),#/music/
#    #url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    
#     ]

urlpatterns=[
    #/music/20/
    url(r'^(?P<pk>\d+)/$', views.DetailsView.as_view(), name='albumdetails'),
    
    #/music/
    url(r'^$', views.Indexview.as_view(), name='index'),
 
    #/ralbums/----for the album json data
    url(r'^ralbums/', views.AlbumList.as_view()),

    #/rsongs/----for the song json data
    url(r'^rsongs/', views.SongList.as_view()),

    #music/album/add
    url(r'albums/add/$', views.AlbumCreate.as_view(), name='add-album'),

    #url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),#/music/<id>/favorite/

    #music/album/2
    url(r'album/(?P<id>d+)/$', views.AlbumUpdate.as_view(), name='album-edit'),

    #music/album/2/delete
     url(r'album/(?P<id>d+)/delete/$', views.Albumdelete.as_view(), name='album-delete'),

     #login/registration form
     url(r'^register/$', views.UserFromView.as_view(), name='register'),
    ]

urlpatterns=format_suffix_patterns(urlpatterns)