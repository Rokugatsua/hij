from django.db import models

# Create your models here.
class Author(models.Model):
    name_author = models.CharField(max_length=100)
     
    def __str__(self):
        return self.name_author


class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.headline


class Artist(models.Model):
    name = models.CharField(max_length=200)
    photo = models.URLField()

    def __str__(self):
        return self.name
    

class Album(models.Model):
    title = models.CharField(max_length=200)
    rel_date = models.DateTimeField()
    label = models.CharField(max_length=200)
    cover_art = models.URLField()               #using urlfield for urlrefrence
    
    def __str__(self):
        return self.title

    
class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    composer = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    year = models.DateField()

    def __str__(self):
        return self.title