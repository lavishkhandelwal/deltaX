from django.db import models
from artists.models import Artist
from django.core.validators import MaxValueValidator, MinValueValidator

class Song(models.Model):
    name = models.CharField(max_length = 30)
    dor = models.DateField()
    cover = models.ImageField(upload_to = 'media/')
    artist = models.ManyToManyField(Artist, blank = True, related_name = 'songs')
    rate = models.FloatField(default = 0)
    total = models.IntegerField(default = 0)

    def get_artists(self):
        return ", ".join([str(a) for a in self.artist.all()])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Songs"