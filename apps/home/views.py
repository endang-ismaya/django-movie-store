from django.shortcuts import render

# Create your views here.


def index(request):
    """home index view"""
    context = {}
    return render(request, "home/index.html", context)


def about(request):
    """about view"""
    context = {}
    return render(request, "home/about.html", context)
