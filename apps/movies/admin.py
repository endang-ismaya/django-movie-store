from django.contrib import admin

from apps.movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    ordering = ["name"]
    search_fields = ["name", "description"]
