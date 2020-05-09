from django.contrib import admin

from .models import Artist, Album, Song

# Register your models here.
@admin.register(Artist, Album, Song)
class hijadmin(admin.ModelAdmin):
    pass