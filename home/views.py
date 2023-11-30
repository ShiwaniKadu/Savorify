from django.shortcuts import render, redirect
from .models import Home
import datetime

# Create your views here.


def index(request):
    context = {
        "title": "Savorify",
        "year": datetime.datetime.now().year,
    }
    if request.method == "POST":
        home = Home()
        home.recipe_name = request.POST.get("recipe_name")
        home.recipe_description = request.POST.get("recipe_description")
        home.recipe_image = request.FILES.get("recipe_image")
        home.save()

        return redirect("/")

    return render(request, "index.html", context)
