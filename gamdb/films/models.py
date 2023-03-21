from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    director = models.ForeignKey('Director', blank=True, null=True, on_delete=models.SET_NULL)
    genres = models.ManyToManyField('Genre', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.year})"

    def genres_display(self):
        return ", ".join([i.name for i in self.genres.all()])
        # out = ""
        # for i in self.genres.all():
        #     out += f"{i.name}, "
        # return out

class Director(models.Model):
    name = models.CharField(max_length=255)
    birth_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.birth_year})"

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
