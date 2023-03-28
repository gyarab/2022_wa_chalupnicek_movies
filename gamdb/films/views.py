from django.shortcuts import render
from .models import Movie

def homepage(request):
    context = {
        "movies": Movie.objects.all()
    }

    return render(request, 'main.html', context)
# Create your views here.
