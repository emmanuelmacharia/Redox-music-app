"""
Definition of models.
"""

from django.db import models
from django.core.urlresolvers import reverse 

# Create your models here.
class Albums(models.Model):
    artist =models.CharField(max_length=50)
    album_Title= models.CharField(max_length=300)
    album_Year=models.CharField(max_length=20)
    genre=models.CharField(max_length=50)
    album_art=models.FileField()

    def get_absolute_url(self):
        return reverse('app:albumdetails', kwargs={'pk':self.pk})

    def __str__(self):
        return self.album_Title + ' by ' + self.artist

class Songs(models.Model):
    album=models.ForeignKey(Albums, on_delete= models.CASCADE)
    file_type=models.CharField(max_length=100)
    song_title=models.CharField(max_length=100)
    song_lyrics=models.TextField(max_length=15000)
    is_favorite=models.BooleanField(default=False)

    def __str__(self):
        return self.song_title


#Django autocreates a primary key for instances in the table by (id=1) and so forth
#primary keys are the Unique ID numbers- for each instance of the class
#We need a way to link two tables together and that is where the Freign Key comes in
#on_delete=models.CASCADE- when an instance from (for example) Album is deleted, the instances linked to that album should be deleted too 

#DJANGO DATABASE API
