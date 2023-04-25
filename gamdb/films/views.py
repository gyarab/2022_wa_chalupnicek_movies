from django.shortcuts import render
from .models import Movie, Director, Actor, Genre
from django.db.models import Q

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
    movies_queryset = Movie.objects.all()
    genre = request.GET.get('genre')
    if genre:
        movies_queryset = movies_queryset.filter(genres__name=genre)
    search = request.GET.get('search')
    if search:
        movies_queryset = movies_queryset.filter(Q(name__icontains=search)|Q(description__icontains=search)) 

    context = {
        "movies": movies_queryset,
        "genres": Genre.objects.all().order_by('name'),
        "genre": genre,
        "search": search,
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
  