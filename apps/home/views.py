from django.shortcuts import render

# Create your views here.


def index(request):
    """home index view"""
    template_data = {}
    template_data["title"] = "Movies Store"
    context = {"template_data": template_data}
    return render(request, "home/index.html", context)


def about(request):
    """about view"""
    template_data = {}
    template_data["title"] = "About"
    context = {"template_data": template_data}
    return render(request, "home/about.html", context)
