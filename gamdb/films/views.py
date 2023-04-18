from django.shortcuts import render
from .models import Movie, Director, Actor, Genre

def directors(request):
    context = {
        'directors': Director.objects.all()
    }
    print(context)
    return render(request, 'directors.html', context)

def director(request, id):
    context = {
        "director": Director.objects.get(id=id)
    }
    return render(request, 'director.html', context)

def movies(request):
    context = {
        "movies": Movie.objects.all()
    }
    return render(request, 'movies.html', context)

def movie(request, id):
    context = {
        "movie": Movie.objects.get(id=id)
    }
    return render(request, 'movie.html', context)

def actors(request):
    context = {
        "actors": Actor.objects.all()
    }
    return render(request, 'actors.html', context)

def actor(request, id):
    context = {
        "actor": Actor.objects.get(id=id)
    }
    return render(request, 'actor.html', context)

def homepage(request):
    context = {
        # TODO use first 10 top rated
        "movies": Movie.objects.all(),
        "actors": Actor.objects.all(),
        "directors": Director.objects.all(),
        "genres": Genre.objects.all(),
    }
    return render(request, 'homepage.html', context)
  