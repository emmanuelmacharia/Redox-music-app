from .models import Albums, Songs
from rest_framework import serializers

class AlbumsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Albums
        fields='__all__'



class SongsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Songs
        fields='__all__'