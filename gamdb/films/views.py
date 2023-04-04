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


def homepage(request):
    context = {
        "movies": Movie.objects.all()
    }

    return render(request, 'main.html', context)

