from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length = 30)
    dob = models.DateField()
    bio = models.TextField()
    rate = rate = models.FloatField(default = 0)

    def __str__(self):
        return self.name