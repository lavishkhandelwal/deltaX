from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Ratings(models.Model):
    rating = models.IntegerField(default = 0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )
    song = models.ForeignKey('songs.Song', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.song.name + ' - ' + self.user.username + ' - ' + str(self.rating)

    class Meta:
        verbose_name_plural = "Ratings"