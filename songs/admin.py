from .models import Song
from django.contrib import admin

# Register your models here.
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'dor', 'cover', 'get_artists', 'rate', 'total',)