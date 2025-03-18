from django.contrib import admin

from apps.movies.models import Movie, Review


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    ordering = ["name"]
    search_fields = ["name", "description"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
