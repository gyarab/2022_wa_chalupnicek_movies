from django.shortcuts import render
from .models import Movie, Director

def directors(request):
    context = {
        'logic': True,
        'title': "Nejoblíbenější režiséři",
        'directors': Director.objects.all()
    }
    print(context)
    return render(request, 'directors.html', context)


def movies(request):
    context = {
        "movies": Movie.objects.all()
    }
    return render(request, 'movies.html', context)

def homepage(request):
    context = {
        # TODO use first 10 top rated
        "movies": Movie.objects.all()
    }
    return render(request, 'homepage.html', context)
  