from django.contrib import admin
from .models import Ratings

# Register your models here.
@admin.register(Ratings)
class RatingsAdmin(admin.ModelAdmin):
    list_display = ('song', 'user', 'rating',)