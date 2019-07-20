from django.views import generic
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from music import views
from .models import Albums, Songs

from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect

from django.contrib.auth import authenticate,login
from .forms import UserForm
from django.core.urlresolvers import reverse_lazy

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import AlbumsSerializer, SongsSerializer
from rest_framework import viewsets

class Indexview(generic.ListView):
    template_name= 'music/Home.html'
    def get_queryset(self):
        return Albums.objects.all()
        context_object_name= 'all_albums'
        #object_list=all_albums


class DetailsView(generic.DetailView):
    model= Albums
    context_object_name='album_detail'
    template_name= 'music/albumdetails.html'
    

class AlbumCreate(CreateView):
    model=Albums
    fields=['artist', 'album_Title', 'album_Year', 'genre', 'album_art']
    template_name='music/albums_form.html'

class AlbumUpdate(UpdateView):
    model=Albums
    fields=['artist', 'album_Title', 'album_Year', 'genre', 'album_art']
    template_name='music/albums_form.html'

class Albumdelete(DeleteView):
    model=Albums
    success_url=reverse_lazy('music:index')


#def albumdetail(request, album_id):
#     album=get_object_or_404(Albums, pk=id)
#     return render(request, 'music/albumdetails.html', {'album':album } )


class UserFromView(View):
    form_class= UserForm
    template_name= 'music/registration_form.html'

    def get(self, request):
        '''displays a blank form'''
        form=self.form_class(None)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        '''processes form data'''
        form= self.form_class(request.POST)

        if form.is_valid():
            user =form.save(commit=False)

           #clean, normalized data
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()


            #returns User object if credentials are correct
            user=authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')
                else:
                    return render(request, self.template_name, {'form':form})

class AlbumList(APIView):
    
    def get(self):
        '''lists all albums in JSON'''
        albums=Albums.objects.all()
        serializer=AlbumsSerializer(albums, many=True)
        return Response(serializer.data)

    def post(self):
        '''lets you edit/add/change'''
        pass

class SongList(APIView):

    def get(self):
        '''lists all stocks in JSON'''
        songs=Songs.objects.all()
        serializer=SongsSerializer(songs, many=True)
        return Response(serializer.data)

    def post(self):
        '''lets you edit/add/change'''
        pass

class Albumview(viewsets.ModelViewSet):
    pass