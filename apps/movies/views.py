from django.shortcuts import render

from apps.movies.models import Movie


def index(request):
    search_term = request.GET.get("search")
    if search_term:
        movies = Movie.objects.filter(name__icontains=search_term)
    else:
        movies = Movie.objects.all()

    template_data = {}
    template_data["title"] = "Movies"
    template_data["movies"] = movies
    context = {"template_data": template_data}
    return render(request, "movies/index.html", context)


def show(request, id):
    movie = Movie.objects.get(id=id)
    template_data = {}
    template_data["title"] = movie.name
    template_data["movie"] = movie
    context = {"template_data": template_data}
    return render(request, "movies/show.html", context)
